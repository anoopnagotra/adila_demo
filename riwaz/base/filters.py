import operator
from functools import reduce

from django.db.models import Q, Case, When, Value, F, fields
from django.db.models.functions import Cast

from riwaz.base.constants import (FILTER_ARGS_CHOICES, ORDER_CHOICES, QUERY_PLACEMENT_CHOICES,
                                       QUERY_PLACEMENT_MAPPING)
from riwaz.base.services.regex_parser import QueryRegex, NumberRegexService
from riwaz.number.models import Numbers, Wishlist
from riwaz.category_numbers.models import Category_numbers, Category_tag
from django.db.models import Value
from django.db.models.functions import Replace, Length

qr = QueryRegex()
nrs = NumberRegexService()


def get_wishlist_numbers(request):
    if request.user.is_authenticated:
        return Wishlist.objects.filter(user=request.user).values_list('number__display_number', flat=True)
    return []


def get_premium_numbers(category):
    return Numbers.objects.select_related('user').filter(
        category_numbers__category=category, user__is_premium=True,
        user__is_active=True, number_status='1').order_by('?')


def sort_by_order(sort_order, mainNumbers):
    order_by = ORDER_CHOICES.get(sort_order)
    if sort_order:
        if sort_order == 'asc':
            mainNumbers = mainNumbers.annotate(number=Cast('number_for_search', output_field=fields.FloatField())).all().order_by('number')
        elif sort_order == 'desc':
            mainNumbers = mainNumbers.annotate(number=Cast('number_for_search', output_field=fields.FloatField())).all().order_by('-number')
        else:
            mainNumbers = mainNumbers.order_by(order_by)
    return mainNumbers


def filter_by_placement(qryPlacement, matchData, matchNumbers):
    if qryPlacement and qryPlacement in QUERY_PLACEMENT_CHOICES:
        matchNumbers = matchNumbers.filter(
            user__is_premium=True,
            user__is_active=True,
            number_status=1,
            **{QUERY_PLACEMENT_CHOICES[qryPlacement]: matchData}
        )
    return matchNumbers



""" Function Ends"""

"""
Method:             sort_number_level_one
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""


def filter_numbers_qs(request, url_match, sort_order, total_in_url, sum_in_url, price, start, tags, cod, matchNumbers, rtp, isAll=False, desc='false', **kwrgs):
    kwargs = dict()
    args = list()
    json_booleans = ['true', 'false']

    if not isAll:
        kwargs['user__is_premium'] = True
    # cod
    if 'cod' in url_match and cod and cod in json_booleans :
        kwargs[FILTER_ARGS_CHOICES["cod"]] = True if cod == 'true' else False
    if 'rtp' in url_match and rtp and rtp in json_booleans:
        kwargs[FILTER_ARGS_CHOICES["rtp"]] = True if not rtp or not rtp == 'false' else False
    # total and sum
    if 'total' in url_match and 'sum' in url_match and total_in_url and sum_in_url:
        args.append(reduce(operator.or_, (comma_saperated_or_filter(sum_in_url, "sum"), comma_saperated_or_filter(total_in_url, "total"))))
    elif 'total' in url_match and total_in_url:
        args.append(comma_saperated_or_filter(total_in_url, "total"))
        # kwargs[FILTER_ARGS_CHOICES["total"]] = total_in_url
    elif 'sum' in url_match and sum_in_url:
        args.append(comma_saperated_or_filter(sum_in_url, "sum"))
        # kwargs[FILTER_ARGS_CHOICES["sum"]] = sum_in_url
    # #price range is passed
    if 'price' in url_match and price:
        kwargs[FILTER_ARGS_CHOICES["price"]] = (price[0], price[1])
    # starts filter is passed
    if 'start' in url_match and start:
        query = reduce(operator.or_, (Q(number_for_search__istartswith=x) for x in start))
        args.append(query)
    # if 'tags' in url_match:
    #     tag_ids = Category_tag.objects.filter(reduce(operator.or_, (Q(id=x) for x in tags))).values_list('id', flat=True).distinct()
    #     filter = reduce(operator.or_, (Q(category_numbers__category_tag_ids__icontains=x) for x in tag_ids))
    #     args.append(filter)

    matchNumbers = matchNumbers.filter(*args, **kwargs)

    if 'sortby' in url_match:
        matchNumbers = sort_by_order(sort_order, matchNumbers)
    return matchNumbers


def sort_numbers_by_filter(request, url_match, my_wishlist_numbers: list, matchNumbers: list=None, serialize: bool=True, is_basic_all=None) -> list:
    total_in_url = request.GET.get('total', None)
    sum_in_url = request.GET.get('sum', None)
    price = request.GET.get('price', None)
    price = list(price.split("-")) if price else None
    sort_order = request.GET.get('sortby', None)
    start = request.GET.get('start', None)
    start = list(start.split(",")) if start else None
    tags = request.GET.get('tags', None)
    tags = tags.split(',') if tags else None
    is_basic = request.GET.get('is_basic', None)
    isAll = True if is_basic == 'all' else False
    rtp = request.GET.get('rtp', None)
    cod = request.GET.get('cod', None)
    desc = request.GET.get('desc', None)

    if is_basic_all:
        isAll = True

    matchNumbers = filter_numbers_qs(request, url_match, sort_order, total_in_url, sum_in_url, price, start, tags, cod, matchNumbers, rtp, isAll, desc)
    if serialize:
        matchNumbers = serialize_numbers(matchNumbers, my_wishlist_numbers)
    return matchNumbers


def serialize_categories(categories):
    category_data = list()
    for category in categories:
        category_dict = dict()
        category_dict["pk"] = category.pk
        category_dict["name"] = category.name
        category_dict["slug"] = category.slug
        category_data.append(category_dict)
    return category_data


def serialize_category_groups(groups):
    data = list()
    for group in groups:
        group_dict = dict()
        group_dict["pk"] = group.pk
        group_dict["type"] = 'group'
        group_dict["name"] = group.name
        group_dict["slug"] = group.slug
        group_dict["categories"] = serialize_categories(group.group_categories)
        data.append(group_dict)
    return data


def serialize_numbers(mainNumbers: list, my_wishlist_numbers: list) -> list:
    num_list = list()
    for mainNumber in mainNumbers:
        num_data = dict()
        num_data['isWishlist'] = True if mainNumber.display_number in my_wishlist_numbers else False
        # todo: No need to serialize here above [isWishlist] field could be evaluted in template while rendering response

        num_data['id'] = mainNumber.id
        num_data['display_number'] = mainNumber.display_number
        num_data['purchase_price'] = mainNumber.selling_price
        num_data['total_views'] = mainNumber.total_views
        num_data['total_likes'] = mainNumber.total_likes
        num_data['total_sum'] = mainNumber.number_total
        num_data['end_sum'] = mainNumber.number_sum
        num_data['rtp'] = mainNumber.rtp
        num_data['tag_premium'] = mainNumber.user.premium_seller_tag
        num_data['rating'] = mainNumber.user.seller_rating
        num_data['premium'] = mainNumber.user.is_premium
        num_data['cod'] = mainNumber.cod
        if num_data not in num_list:
            num_list.append(num_data)
    return num_list


def serialize_valued_admin_numbers(mainNumbers: list, my_wishlist_numbers: list, prefix: str='', category_tags=False) -> list:
    num_list = list()
    for mainNumber in mainNumbers:
        num_data = dict()
        num_data['isWishlist'] = True if mainNumber[prefix + 'display_number'] in my_wishlist_numbers else False
        num_data['id'] = mainNumber[prefix + 'id']
        num_data['display_number'] = mainNumber[prefix + 'display_number']
        num_data['purchase_price'] = mainNumber[prefix + 'selling_price']
        num_data['total_views'] = mainNumber[prefix + 'total_views']
        num_data['total_likes'] = mainNumber[prefix + 'total_likes']
        num_data['total_sum'] = mainNumber[prefix + 'number_total']
        num_data['end_sum'] = mainNumber[prefix + 'number_sum']
        num_data['rtp'] = mainNumber[prefix + 'rtp']
        num_data['tag_premium'] = mainNumber[prefix + 'user__premium_seller_tag']
        num_data['rating'] = mainNumber[prefix + 'user__seller_rating']
        num_data['premium'] = mainNumber[prefix + 'user__is_premium']
        num_data['cod'] = mainNumber[prefix + 'cod']
        num_data['user'] = mainNumber[prefix + 'user__name']
        num_data['created_at'] = mainNumber[prefix + 'created_at']
        num_data['group_number'] = mainNumber[prefix + 'group_number']
        if category_tags:
            cat_numbers = Category_numbers.objects.filter(number_id=num_data['id'])
            if cat_numbers.exists():
                all_tag_ids = set()
                categories = set()
                for cat_number in cat_numbers:
                    categories.add(cat_number.category.name)
                    tag_ids = cat_number.category_tag_ids
                    tag_ids = tag_ids.split(",") if tag_ids else  []
                    all_tag_ids = all_tag_ids.union(tag_ids)
                num_data['categories'] = categories
                tags = Category_tag.objects.filter(id__in=all_tag_ids)
                num_data["tags"] = [tag.name for tag in tags]
        if num_data not in num_list:
            num_list.append(num_data)
    return num_list


def serialize_numbers_with_values(suggested_numbers: list, my_wishlist_numbers: list, limit: int=120) -> list:
    suggested_numbers = suggested_numbers.values('id','display_number', 'selling_price', 'selling_price', 'total_views', 'total_likes', 'number_total',
                 'number_sum', 'rtp', 'user__premium_seller_tag', 'user__seller_rating', 'user__is_premium', 'cod')[:limit]
    return serialize_valued_numbers(suggested_numbers, my_wishlist_numbers)


def serialize_valued_numbers(mainNumbers, my_wishlist_numbers, prefix=''):
    num_list = list()
    for mainNumber in mainNumbers:
        num_data = dict()
        num_data['isWishlist'] = True if mainNumber[prefix + 'display_number'] in my_wishlist_numbers else False
        num_data['id'] = mainNumber[prefix + 'id']
        num_data['display_number'] = mainNumber[prefix + 'display_number']
        num_data['purchase_price'] = mainNumber[prefix + 'selling_price']
        num_data['total_views'] = mainNumber[prefix + 'total_views']
        num_data['total_likes'] = mainNumber[prefix + 'total_likes']
        num_data['total_sum'] = mainNumber[prefix + 'number_total']
        num_data['end_sum'] = mainNumber[prefix + 'number_sum']
        num_data['rtp'] = mainNumber[prefix + 'rtp']
        num_data['tag_premium'] = mainNumber[prefix + 'user__premium_seller_tag']
        num_data['rating'] = mainNumber[prefix + 'user__seller_rating']
        num_data['premium'] = mainNumber[prefix + 'user__is_premium']
        num_data['cod'] = mainNumber[prefix + 'cod']
        if num_data not in num_list:
            num_list.append(num_data)
    return num_list


def get_start_with_suggestion_keywords(search_word: str) -> list:
    return [] if len(search_word) < 2 else [search_word[:index] for index in range(1, len(search_word))][::-1]


def get_end_with_suggestion_keywords(search_word: str) -> list:
    if len(search_word) < 3:
        return []
    asc_keys = [search_word[:index] for index in range(2, len(search_word))][::-1]
    desc_keys = [search_word[index:] for index in range(1, len(search_word)-1)]
    return list(set(asc_keys + desc_keys))


def get_anywhere_suggestion_keywords(search_word: str) -> list:
    if len(search_word) < 4:
        return []
    asc_keys = [search_word[:index] for index in range(3, len(search_word))][::-1]
    desc_keys = [search_word[index:] for index in range(1, len(search_word)-2)]
    return list(set(asc_keys + desc_keys))


def get_suggestion_keywords(search_word, query_param):
    if query_param == 'start_with':
        return get_start_with_suggestion_keywords(search_word)
    if query_param == 'end_with':
        return get_end_with_suggestion_keywords(search_word)
    if query_param == 'anywhere':
        return get_anywhere_suggestion_keywords(search_word)


def must_contains(request, match_number):
    contains_list = request.GET.get("must_contains")
    if contains_list:
        query_filter = reduce(operator.and_, (
            Q(**{FILTER_ARGS_CHOICES["search_re"]: qr.get_qs_regex(x, 'must_contains')})
            for x in contains_list.split(",") if x))
        match_number = match_number.filter(query_filter)
    return match_number


def not_contains(request, match_number):
    contains_list = request.GET.get("not_contains")

    if contains_list:
        query_filter = [Q(**{FILTER_ARGS_CHOICES["search_re"]: qr.get_qs_regex(x, 'not_contains')})
                for x in contains_list.split(",") if x]
        for query in query_filter:
            match_number = match_number.exclude(query)
    return match_number


def any_contains(request, match_number):
    contains_list = request.GET.get("any_contains")
    if contains_list:
        query_filter = reduce(operator.or_, (
            Q(**{FILTER_ARGS_CHOICES["search_re"]: qr.get_qs_regex(x, 'any_contains')})
            for x in contains_list.split(",") if x))
        match_number = match_number.filter(query_filter)
    return match_number


def comma_saperated_or_filter(comma_separated_values, filter_arg, regex_mapper='anywhere'):
    return reduce(operator.or_, (
            Q(**{FILTER_ARGS_CHOICES[filter_arg]: qr.get_qs_regex(x, regex_mapper)})
            for x in comma_separated_values.split(",") if x))


def start_end_anywhere_filter(request, search_number):
    query = Q()
    if request.GET.get("start_with"):
        query &= comma_saperated_or_filter(request.GET["start_with"],  'search_re', "start_with")
    if request.GET.get("end_with"):
        query &= comma_saperated_or_filter(request.GET["end_with"],  'search_re', "end_with")
    if request.GET.get("anywhere"):
        query &= comma_saperated_or_filter(request.GET["anywhere"],  'search_re', "anywhere")
    return search_number.filter(query)


def search_filter_query_builder(request, query_param):
    search_words = get_suggestion_keywords(request.GET[query_param], query_param)
    if search_words:
        query_filter = reduce(operator.or_, (Q(**{FILTER_ARGS_CHOICES['search_re']: qr.get_qs_regex(x, query_param), }) for x in search_words if x))
        query_exclude = Q(**{FILTER_ARGS_CHOICES['search_re']: qr.get_qs_regex(request.GET[query_param], query_param)})
    else:
        query_exclude = query_filter = Q()
    return query_filter, query_exclude


def start_end_anywhere_suggested_filter(request, matchNumber):
    filter_query, exclude_query = list(), list()
    start_with = request.GET.get("start_with", "")
    end_with = request.GET.get("end_with", "")
    anywhere = request.GET.get("anywhere", "")

    if len(start_with) > 1 or len(end_with) > 2 or len(anywhere) > 3:
        if start_with:
            f, e = search_filter_query_builder(request, "start_with")
            filter_query.append(f)
            exclude_query.append(e)
        if end_with:
            f, e = search_filter_query_builder(request, "end_with")
            filter_query.append(f)
            exclude_query.append(e)
        if anywhere:
            f, e = search_filter_query_builder(request, "anywhere")
            filter_query.append(f)
            exclude_query.append(e)

        if filter_query:
            filter_query = reduce(operator.or_, (x for x in filter_query if x))
            exclude_query = reduce(operator.and_, (x for x in exclude_query if x))
            return matchNumber.filter(filter_query).exclude(exclude_query)
    return Numbers.objects.none()


def advance_search_contains_filter(request, matchNumber, suggested=False):
    if suggested:
        matchNumber = start_end_anywhere_suggested_filter(request, matchNumber)
    else:
        matchNumber = start_end_anywhere_filter(request, matchNumber)
    matchNumber = must_contains(request, matchNumber)
    matchNumber = not_contains(request, matchNumber)
    matchNumber = any_contains_with_max_match_sorting(request, matchNumber)
    matchNumber = most_contains(request, matchNumber)
    return matchNumber


def most_contains(request, numbers_qs):
    search = request.GET["most_contains"].split(",")[0] if request.GET.get("most_contains") else None
    search = nrs.sanitize_number_to_search(search)
    if search:
        numbers_qs = numbers_qs.filter(number_for_search__contains=search).annotate(
            most_search=Replace('number_for_search', Value(search), Value(''))).values('number_for_search', 'most_search').order_by(
            Length('most_search').asc())
    return numbers_qs


def any_contains_with_max_match_sorting(request, matchNumber):
    contains_list = request.GET["any_contains"].split(",") if request.GET.get("any_contains") else None
    if contains_list:
        filter_query, cases = Q(), dict()
        for i, keyword in enumerate(contains_list):
            re_word = qr.get_qs_regex(keyword)
            filter_query |= Q(**{FILTER_ARGS_CHOICES["search_re"]: re_word})
            cases[f'keyword_match_{i}'] = Case(
                When(number_for_search__regex=re_word, then=1),
                default=Value(0),
                output_field=fields.IntegerField(),
            )
        matchNumber = matchNumber.filter(filter_query).annotate(**cases).annotate(
            keywords_matched=reduce(operator.add, (F(name) for name in cases))).order_by('-keywords_matched')
    return matchNumber


def most_contains_tags_with_max_match_sorting(matchNumber, tags):
    from django.db.models import Case, When, Value, F, fields
    from operator import add
    filter, cases = Q(), dict()
    for i, keyword in enumerate(tags):
        filter |= Q(category_tag_ids__contains=keyword)
        cases[f'keyword_match_{i}'] = Case(
            When(category_tag_ids__contains=keyword, then=1),
            default=Value(0),
            output_field=fields.IntegerField(),
        )
    matchNumber = matchNumber.filter(filter).annotate(**cases).annotate(
        keywords_matched=reduce(add, (F(name) for name in cases))).order_by('-keywords_matched')
    return matchNumber


QUERY_PLACEMENT_SUGGESTION_FUNCTION_MAPPING = {
    '1': get_start_with_suggestion_keywords,
    '2': get_anywhere_suggestion_keywords,
    '3': get_end_with_suggestion_keywords,
}


def search_placement_filter(search_word, query_placement, match_numbers, suggested_numbers):
    query = Q()
    query_param = QUERY_PLACEMENT_MAPPING[query_placement]
    no_number = Numbers.objects.none()

    match_numbers = match_numbers.filter(number_for_search__regex=qr.get_qs_regex(search_word, query_param))
    searchData = QUERY_PLACEMENT_SUGGESTION_FUNCTION_MAPPING[query_placement](search_word)
    if searchData:
        for search in searchData:
            query = query | Q(number_for_search__regex=qr.get_qs_regex(search, query_param))
        suggested_numbers = suggested_numbers.filter(query).exclude(
            number_for_search__regex=qr.get_qs_regex(search_word, query_param)).order_by('-purchase_price')
    else:
        suggested_numbers = no_number
    return match_numbers, suggested_numbers
