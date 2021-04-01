URL_MATCH = "total|sum|price|sortby|tags|start|rtp|cod|is_basic|desc"

ADVANCE_SEARCH_URL_MATCH = "total|sum|price|sortby|tags|start|rtp|cod|is_basic|desc|start_with|anywhere|end_with"

ORDER_CHOICES = {
    'high_to_low': '-purchase_price',
    'low_to_high': 'purchase_price',
    'likes': '-total_likes',
    'most_view': '-total_views',
    'similarity': 'group_number',
}

QUERY_PLACEMENT_CHOICES = {
    '1': "number_for_search__istartswith",
    '2': "number_for_search__icontains",
    '3': "number_for_search__iendswith"
}

FILTER_ARGS_CHOICES = {
    'cod': 'cod',
    'total': 'number_total',
    'price': 'selling_price__range',
    'sum': 'number_sum',
    'start': 'number_for_search__istartswith',
    'rtp': 'rtp',
    'is_basic': 'user__is_premium',
    'start_with': 'number_for_search__istartswith',
    'anywhere': 'number_for_search__icontains',
    'end_with': 'number_for_search__iendswith',
    'contains': 'number_for_search__contains',
    'search_re': 'number_for_search__regex',
}

ALLOWED_NUMBER_REGEX_KEYS = [f'{number}' for number in range(10)] + ['*']

ALLOWED_SPECIAL_CHARACTERS = ['-', ' ', '_', ]
ALLOWED_DISPLAY_NUMBER_REGEX_KEYS = [f'{number}' for number in range(10)] + ALLOWED_SPECIAL_CHARACTERS


QUERY_PLACEMENT_MAPPING = {
    '1': 'start_with',
    '2': 'anywhere',
    '3': 'end_with',
}
