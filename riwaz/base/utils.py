from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from riwaz.categories.models import Categories
from riwaz.category_tag.models import Category_tag
from riwaz.category_numbers.models import Category_numbers
from riwaz.number.models import Numbers
from riwaz.number.models import Wishlist
from riwaz.users.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core import serializers
from riwaz.base.utils import Category_numbers
from django.db.models import Q
from itertools import chain


# from models import User
import json
import datetime
import random 


def get_categories(number_qs, sug_numbers_qs):
    return ",".join(map(str, set(Categories.objects.filter(category_numbers__number__in=number_qs).values_list('id', flat=True).order_by('id')).union(
		set(Categories.objects.filter(category_numbers__number__in=sug_numbers_qs).values_list('id', flat=True).order_by('id')[:60]))))


"""
Method:             get_premium_numbers
Developer:          Anoop Kumar
Created Date:       29-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def get_premium_numbers(request, category, my_wishlist_numbers):
	numbers = Category_numbers.objects.select_related('number', 'number__user').filter(category_id = category.id, number__user__is_premium=True,number__user__is_active=True, number__number_status = '1')#.order_by('?')
	premium_numbers = []
	for number in numbers:
		# if number.number.user.is_active:
		# 	if number.number.user.is_premium:
		# 		if str(number.number.number_status) == str(1):
		num_data = {'isWishlist' : False}
		if number.number.display_number in my_wishlist_numbers:
			num_data['isWishlist'] = True

		num_data['id'] = number.number_id
		num_data['display_number'] = number.number.display_number
		num_data['purchase_price'] = number.number.selling_price
		num_data['total_views'] = number.number.total_views
		num_data['total_likes'] = number.number.total_likes
		num_data['total_sum'] = number.number.number_total
		num_data['end_sum'] = number.number.number_sum
		num_data['rtp'] = number.number.rtp
		num_data['cod'] = number.number.cod
		num_data['premium'] = True
		num_data['tag_premium'] = number.number.user.premium_seller_tag
		num_data['rating'] = number.number.user.seller_rating
		num_data['rtp_date'] = number.number.rtp_date
		premium_numbers.append(num_data)
				
	random.shuffle(premium_numbers)
	return premium_numbers
""" Function Ends"""
"""
Method:             get_premium_numbers
Developer:          Anoop Kumar
Created Date:       29-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def get_premium_numbers_for_tagfilter(request, numbers, my_wishlist_numbers):
	premium_numbers = []
	for num_id in numbers:
		# print()
		number = Numbers.objects.filter(id=num_id[0]).first()
		# print(number)
		# for number in mainNumbers:
		if number.user.is_active:
			if number.user.is_premium:
				if str(number.number_status) == str(1):
					num_data = {'isWishlist' : False}
					if number.display_number in my_wishlist_numbers:
						num_data['isWishlist'] = True

					num_data['id'] = number.id
					num_data['display_number'] = number.display_number
					num_data['purchase_price'] = number.selling_price
					num_data['total_views'] = number.total_views
					num_data['total_likes'] = number.total_likes
					num_data['total_sum'] = number.number_total
					num_data['end_sum'] = number.number_sum
					num_data['rtp'] = number.rtp
					num_data['cod'] = number.cod
					num_data['premium'] = True
					num_data['tag_premium'] = number.user.premium_seller_tag
					num_data['rating'] = number.user.seller_rating
					premium_numbers.append(num_data)
					
	random.shuffle(premium_numbers)
	return premium_numbers
""" Function Ends"""
"""
Method:             get_premium_numbers
Developer:          Anoop Kumar
Created Date:       29-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def get_premium_numbers_by_tagfilter(request, numbers, my_wishlist_numbers):
	premium_numbers = []
	for number in numbers:
		# if str(number.number__number_status) == str(1):
		num_data = {'isWishlist' : False}
		if number.number.display_number in my_wishlist_numbers:
			num_data['isWishlist'] = True

		num_data['id'] = number.number.id
		num_data['display_number'] = number.number.display_number
		num_data['purchase_price'] = number.number.selling_price
		num_data['total_views'] = number.number.total_views
		num_data['total_likes'] = number.number.total_likes
		num_data['total_sum'] = number.number.number_total
		num_data['end_sum'] = number.number.number_sum
		num_data['rtp'] = number.number.rtp
		num_data['cod'] = number.number.cod
		num_data['premium'] = True
		num_data['tag_premium'] = number.number.user.premium_seller_tag
		num_data['rating'] = number.number.user.seller_rating
		premium_numbers.append(num_data)
					
	random.shuffle(premium_numbers)
	return premium_numbers
""" Function Ends"""
"""
Method:             get_premium_numbers
Developer:          Anoop Kumar
Created Date:       29-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def get_premium_numbers_for_tags(request, numbers, my_wishlist_numbers):
	premium_numbers = []
	for number in numbers:
		if number.number.user.is_active:
			if number.number.user.is_premium:
				num_data = {'isWishlist' : False}
				if number.number.display_number in my_wishlist_numbers:
					num_data['isWishlist'] = True

				num_data['id'] = number.number.id
				num_data['display_number'] = number.number.display_number
				num_data['purchase_price'] = number.number.selling_price
				num_data['total_views'] = number.number.total_views
				num_data['total_likes'] = number.number.total_likes
				num_data['total_sum'] = number.number.number_total
				num_data['end_sum'] = number.number.number_sum
				num_data['rtp'] = number.number.rtp
				num_data['cod'] = number.number.cod
				num_data['premium'] = True
				num_data['tag_premium'] = number.number.user.premium_seller_tag
				num_data['rating'] = number.number.user.seller_rating
				if num_data not in premium_numbers:
					premium_numbers.append(num_data)
				
	random.shuffle(premium_numbers)
	return premium_numbers
""" Function Ends"""

"""
Method:             get_premium_numbers
Developer:          Anoop Kumar
Created Date:       29-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def post_premium_numbers_for_tags(request, numbers, my_wishlist_numbers):
	print ()
	premium_numbers = []
	for num_id in numbers:
		
		number = Numbers.objects.filter(id=num_id[0]).first()
		
		# for number in mainNumbers:
		if number.user.is_active:
			if number.user.is_premium:
				if str(number.number_status) == str(1):
					num_data = {'isWishlist' : False}
					if number.display_number in my_wishlist_numbers:
						num_data['isWishlist'] = True

					num_data['id'] = number.id
					num_data['display_number'] = number.display_number
					num_data['purchase_price'] = number.selling_price
					num_data['total_views'] = number.total_views
					num_data['total_likes'] = number.total_likes
					num_data['total_sum'] = number.number_total
					num_data['end_sum'] = number.number_sum
					num_data['rtp'] = number.rtp
					num_data['cod'] = number.cod
					num_data['premium'] = True
					num_data['tag_premium'] = number.user.premium_seller_tag
					num_data['rating'] = number.user.seller_rating
					premium_numbers.append(num_data)
					
	random.shuffle(premium_numbers)
	return premium_numbers
""" Function Ends"""

"""
Method:             get_simple_numbers
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def get_simple_numbers(request, category, my_wishlist_numbers):
	cat_numbers = []
	numbers = Category_numbers.objects.filter(category_id = category.id)

	for number in numbers:
		# if number.number.user.is_premium ==False:
		num_data = {}
		num_data['isWishlist'] = False
		if number.number.display_number in my_wishlist_numbers:
			num_data['isWishlist'] = True

		num_data['id'] = number.number.id
		num_data['display_number'] = number.number.display_number
		num_data['purchase_price'] = number.number.selling_price
		num_data['total_views'] = number.number.total_views
		num_data['total_likes'] = number.number.total_likes
		num_data['total_sum'] = number.number.number_total
		num_data['end_sum'] = number.number.number_sum
		num_data['rtp'] = number.number.rtp
		num_data['tag_premium'] = number.number.user.premium_seller_tag
		num_data['rating'] = number.number.user.seller_rating
		if number.number.user.is_premium == True:
			num_data['premium'] = True
		else:
			num_data['premium'] = False
		cat_numbers.append(num_data)
	return cat_numbers

""" Function Ends"""



"""
Method:             get_simple_numbers
Developer:          Aman Preet SIngh
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def serialize_numbers(numbers, my_wishlist_numbers):
	cat_numbers = []
	for number in numbers:
		# if number.number.user.is_premium ==False:
		num_data = dict()
		num_data['isWishlist'] = False
		if number.number.display_number in my_wishlist_numbers:
			num_data['isWishlist'] = True

		num_data['id'] = number.number.id
		num_data['display_number'] = number.number.display_number
		num_data['purchase_price'] = number.number.selling_price
		num_data['total_views'] = number.number.total_views
		num_data['total_likes'] = number.number.total_likes
		num_data['total_sum'] = number.number.number_total
		num_data['end_sum'] = number.number.number_sum
		num_data['rtp'] = number.number.rtp
		num_data['tag_premium'] = number.number.user.premium_seller_tag
		num_data['rating'] = number.number.user.seller_rating
		num_data['premium'] = True if number.number.user.is_premium else False
		cat_numbers.append(num_data)
	return cat_numbers




"""
Method:             sort_numbers
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def sort_numbers(request, num_ids, my_wishlist_numbers, sort_order):
	cat_numbers = []
	try:
		if (sort_order == 'high_to_low'):
			mainNumbers = Numbers.objects.filter(id__in=num_ids).order_by('-purchase_price')
		elif (sort_order == 'low_to_high'):
			mainNumbers = Numbers.objects.filter(id__in=num_ids).order_by('purchase_price')
		elif(sort_order == 'likes'):
			mainNumbers = Numbers.objects.filter(id__in=num_ids).order_by('-total_likes')
		elif(sort_order == 'most_view'):
			mainNumbers = Numbers.objects.filter(id__in=num_ids).order_by('-total_views')
	except Numbers.DoesNotExist:
		mainNumbers = []

	if mainNumbers:
		for mainNumber in mainNumbers:
			if mainNumber.user.is_premium:
				num_data = {}
				num_data['isWishlist'] = False
				if mainNumber.display_number in my_wishlist_numbers:
					num_data['isWishlist'] = True

				num_data['id'] = mainNumber.id
				num_data['display_number'] = mainNumber.display_number
				num_data['purchase_price'] = mainNumber.selling_price
				num_data['total_views'] = mainNumber.total_views
				num_data['total_likes'] = mainNumber.total_likes
				num_data['total_sum'] = mainNumber.number_total
				num_data['end_sum'] = mainNumber.number_sum
				num_data['rtp'] = mainNumber.rtp
				cat_numbers.append(num_data)
	return cat_numbers

""" Function Ends"""

"""
Method:             get_simple_numbers
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def get_wishlist_numbers(request):
	my_wishlist_numbers = []
	wishlist_numbers = Wishlist.objects.select_related('user').filter(user_id = request.user.id).values('number__display_number')
	if wishlist_numbers:
		my_wishlist_numbers = list(wishlist_numbers.values_list('number__display_number', flat = True))

		# for number in wishlist_numbers:
		# 	my_wishlist_numbers.append(number.number.display_number)

	return my_wishlist_numbers

""" Function Ends"""

"""
Method:             numberQuickView
Developer:          Anoop Kumar.
Created Date:       29-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def get_numbers(request,numbers,user_id):
	my_wishlist_numbers = []
	if user_id:
		wishlist_numbers = Wishlist.objects.select_related('user').filter(user_id = user_id)
		if wishlist_numbers:
			for number in wishlist_numbers:
				my_wishlist_numbers.append(number.number.display_number)

	# all_numbers = Numbers.objects.filter(highlight=True).distinct()
	cat_numbers = []
	for number in numbers:
		num_data = {}
		num_data['isWishlist'] = False
		if number.display_number in my_wishlist_numbers:
			num_data['isWishlist'] = True
		num_data['id'] = number.id
		num_data['display_number'] = number.display_number
		num_data['purchase_price'] = number.selling_price
		num_data['total_views'] = number.total_views
		num_data['total_likes'] = number.total_likes
		num_data['total_sum'] = number.number_total
		num_data['end_sum'] = number.number_sum
		num_data['rtp'] = number.rtp
		num_data['cod'] = number.cod
		num_data['tag_premium'] = number.user.premium_seller_tag
		num_data['rating'] = number.user.seller_rating
		cat_numbers.append(num_data)
		# if number.number.user.is_active:
		# 	if number.number.highlight:
		# 		if number.number.user.is_premium:
		# 			if str(number.number.number_status) == str(1):
		# 				num_data = {}
		# 				num_data['isWishlist'] = False
		# 				if number.number.display_number in my_wishlist_numbers:
		# 					num_data['isWishlist'] = True

		# 				num_data['id'] = number.number.id
		# 				num_data['display_number'] = number.number.display_number
		# 				num_data['purchase_price'] = number.number.selling_price
		# 				num_data['total_views'] = number.number.total_views
		# 				num_data['total_likes'] = number.number.total_likes
		# 				num_data['total_sum'] = number.number.number_total
		# 				num_data['end_sum'] = number.number.number_sum
		# 				num_data['rtp'] = number.number.rtp
		# 				num_data['cod'] = number.number.cod
		# 				num_data['tag_premium'] = number.number.user.premium_seller_tag
		# 				num_data['rating'] = number.number.user.seller_rating
		# 				cat_numbers.append(num_data)
	return cat_numbers
""" Function Ends"""

"""
Method:             sort_by_order
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""

ORDER_CHOICES = {
	'high_to_low': '-purchase_price',
	'low_to_high': 'purchase_price',
	'likes': '-total_likes',
	'most_view': '-total_views'
}


def sort_by_order(sort_order, mainNumbers):
	order_by = ORDER_CHOICES.get(sort_order)
	if sort_order:
		mainNumbers = mainNumbers.order_by(order_by)
	return mainNumbers
""" Function Ends"""

"""
Method:             sort_number_level_one
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""

FILTER_ARGS_CHOICES = {
	'cod': 'cod',
	'total': 'number_total',
	'price': 'selling_price__range',
	'sum': 'number_sum',
	'start': 'number_for_search__istartswith',
}

def sort_number_level_one(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod, matchNumbers):
	print("\n***********>>>>    sort_number_level_one  <<<<*************")
	kwargs = dict()
	args = list()

	# sortingmainNumbers
	if 'sortby' in url_match:
		print("\n ***********>>>>    Sorting")
		matchNumbers = sort_by_order(sort_order, matchNumbers)

	# cod
	if 'cod' in url_match:
		kwargs[FILTER_ARGS_CHOICES["cod"]] = cod

	if 'total' in url_match and 'sum' in url_match:
		args.append(Q(number_total=total_in_url) | Q(number_sum=sum_in_url))

	elif 'total' in url_match:
		kwargs[FILTER_ARGS_CHOICES["total"]] = total_in_url

	# #Total filter is passed
	elif 'sum' in url_match:
		kwargs[FILTER_ARGS_CHOICES["sum"]] = sum_in_url

	# #price range is passed
	if 'price' in url_match:
		kwargs[FILTER_ARGS_CHOICES["price"]] = (price[0], price[1])

	# starts filter is passed
	if 'start' in url_match:
		kwargs[FILTER_ARGS_CHOICES["start"]] = start
		# extra(where=["%s LIKE postcode_prefix||'%%'"], params=[postcode]
		

	if 'start' in url_match:
		query = Q()
		for num in start:
			print("num >>  ", num)
			query = query | Q(number_for_search__istartswith=num)
		args.append(query)

	matchNumbers = matchNumbers.filter(*args, **kwargs)

	# starts filter is passed
	if 'tags' in url_match:
		query = Q()
		for slug in tags:
			query = query | Q(slug=slug)

		tag_ids = Category_tag.objects.filter(query).values_list('id', flat=True)
		for tag_id in tag_ids:
			matchNumbers = matchNumbers.filter(category_numbers__category_tag_ids__icontains=tag_id)

	return matchNumbers
""" Function Ends"""
"""
Method:             sort_number_level_two
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def sort_number_level_two(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod):

	print("<<<<<<<<<<<<<<<<	<<<<  inside Level 2 >>>>>>>>>>>>>>>>>>>>>> ")
	
	mainNumbers = []
	if total_in_url and sum_in_url:
		# With OR Conditions
		mainNumbers = Numbers.objects.filter(id__in=num_ids)
		mainNumbers = mainNumbers.filter(Q(number_total=total_in_url)| Q(number_sum=sum_in_url))
	
	# COD and Total
	if total_in_url and cod:
		mainNumbers = Numbers.objects.filter(Q(id__in=num_ids) & Q(number_total=total_in_url) & Q(cod=True))
		mainNumbers1 = Numbers.objects.filter(Q(id__in=num_ids) | (Q(number_total=total_in_url) | Q(cod=False)))
		mainNumbers = chain(mainNumbers, mainNumbers1)
	
	# COD and Sum
	if sum_in_url and cod:
		mainNumbers = Numbers.objects.filter(Q(id__in=num_ids) & Q(number_sum=sum_in_url) & Q(cod=True))
		mainNumbers1 = Numbers.objects.filter(Q(id__in=num_ids) | (Q(number_sum=sum_in_url) | Q(cod=False)))
		mainNumbers = chain(mainNumbers, mainNumbers1)


	#Total and price is passed
	if total_in_url and price:
		mainNumbers = Numbers.objects.filter(
											id__in=num_ids, 
											number_total=total_in_url, 
											selling_price__range=(price[0],price[1])
											)
	#sum and price filter is passed
	if price and sum_in_url:
		mainNumbers = Numbers.objects.filter(
											id__in=num_ids, 
											number_sum=sum_in_url, 
											selling_price__range=(price[0],price[1])
											)

	#price and start filter is passed										
	if price and start:
		query = Q()
		query1 = Q(id__in=num_ids,selling_price__range=(price[0],price[1]))

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		mainNumbers = Numbers.objects.filter(query)

	# COD and Sum
	if price and cod:
		mainNumbers = Numbers.objects.filter(Q(id__in=num_ids) & Q(selling_price__range=(price[0],price[1])) & Q(cod=True))
		mainNumbers1 = Numbers.objects.filter(Q(id__in=num_ids) | Q(selling_price__range=(price[0],price[1])) | Q(cod=False))
		mainNumbers = chain(mainNumbers, mainNumbers1)


	# COD and Sum
	if start and cod:
		query = Q()
		query1 = Q(id__in=num_ids,cod=True)

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		mainNumbers = Numbers.objects.filter(query)

		query = Q()
		query1 = Q(id__in=num_ids,cod=False)

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		mainNumbers1 = Numbers.objects.filter(query)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	#total and start filter is passed
	if total_in_url and start:
		query = Q()
		query1 = Q(id__in=num_ids,number_total=total_in_url)

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		mainNumbers = Numbers.objects.filter(query)
		
	#sum and start filter is passed
	if sum_in_url and start:
		query = Q()
		query1 = Q(id__in=num_ids, number_sum=sum_in_url)

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		mainNumbers = Numbers.objects.filter(query)

	#total and sort_order filter is passed
	if total_in_url and sort_order:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(number_total=total_in_url)
		
	#sum and sort_order filter is passed	
	if sum_in_url and sort_order:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(number_sum=sum_in_url)

	#start and sort_order filter is passed	
	if sort_order and start:
		numbers  = sort_by_order(sort_order,num_ids)
		query = Q()
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)
		mainNumbers =numbers.filter(query)


	#start and sort_order filter is passed	
	if sort_order and cod:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers =numbers.filter(cod=True)
		mainNumbers1 =numbers.filter(cod=False)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	#price and sort_order filter is passed	
	if sort_order and price:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(selling_price__range=(price[0],price[1]))
	
	if total_in_url and tags:
		query = Q()
		for slug in tags:
			query = query | Q(slug=slug)

	
		tagData = Category_tag.objects.filter(query)
		for tag in tagData:
			category_numbers = Category_numbers.objects.filter(category_tag_ids__icontains=tag.id).distinct()
			for nmber in category_numbers:
				
				mainNumbers = Numbers.objects.filter(
											id__in=num_ids,
											number_total=total_in_url
											)

	if sum_in_url and tags:
		query = Q()
		for slug in tags:
			query = query | Q(slug=slug)


		tagData = Category_tag.objects.filter(query)
		for tag in tagData:
			category_numbers = Category_numbers.objects.filter(category_tag_ids__icontains=tag.id).distinct()
			for nmber in category_numbers:
				
				mainNumbers = Numbers.objects.filter(
											id__in=num_ids,
											number_sum=sum_in_url
											)
	if price and tags:
		query = Q()
		for slug in tags:
			query = query | Q(slug=slug)

		tagData = Category_tag.objects.filter(query)
		for tag in tagData:
			category_numbers = Category_numbers.objects.filter(category_tag_ids__icontains=tag.id).distinct()
			for nmber in category_numbers:
				mainNumbers = Numbers.objects.filter(
											id__in=num_ids,
											selling_price__range=(price[0],price[1])
											)

	# 
		# mainNumbers = nums
	print("mainNumbers ==  " , mainNumbers)	
	return mainNumbers



""" Function Ends"""

"""
Method:             sort_number_level_three
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def sort_number_level_three(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod):
	mainNumbers = []

	# COD and Sum
	if cod and price and total_in_url:
		mainNumbers = Numbers.objects.filter(
									id__in=num_ids, 
									selling_price__range=(price[0], price[1]),
									cod=True
									)
		mainNumbers = mainNumbers.filter(Q(number_total=total_in_url))

		mainNumbers1 = Numbers.objects.filter(
									id__in=num_ids, 
									selling_price__range=(price[0], price[1]),
									cod=False
									)
		mainNumbers1 = mainNumbers1.filter(Q(number_total=total_in_url))
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if sum_in_url and price and total_in_url:
		mainNumbers = Numbers.objects.filter(
									id__in=num_ids, 
									selling_price__range=(price[0], price[1])
									)
		mainNumbers = mainNumbers.filter(Q(number_total=total_in_url)| Q(number_sum=sum_in_url))

	if cod and price and sum_in_url:
		mainNumbers = Numbers.objects.filter(
									id__in=num_ids, 
									selling_price__range=(price[0], price[1]),
									cod=True
									)
		mainNumbers = mainNumbers.filter(Q(number_sum=sum_in_url))

		mainNumbers1 = Numbers.objects.filter(
									id__in=num_ids, 
									selling_price__range=(price[0], price[1]),
									cod=False
									)
		
		mainNumbers1 = mainNumbers1.filter(Q(number_sum=sum_in_url))
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if cod and total_in_url and sum_in_url:
		mainNumbers = Numbers.objects.filter(
									id__in=num_ids, 
									cod=True
									)
		mainNumbers = mainNumbers.filter(Q(number_total=total_in_url)| Q(number_sum=sum_in_url))
		
		mainNumbers1 = Numbers.objects.filter(
									id__in=num_ids, 
									cod=False
									)
		mainNumbers1 = mainNumbers1.filter(Q(number_total=total_in_url)| Q(number_sum=sum_in_url))
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if start and price and total_in_url:
		query = Q()
		query1 = Q(id__in=num_ids, number_total=total_in_url, selling_price__range=(price[0],price[1]))

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		mainNumbers = Numbers.objects.filter(query)

	if start and price and cod:
		query = Q()
		query1 = Q(id__in=num_ids, cod=True, selling_price__range=(price[0],price[1]))
		query2 = Q(id__in=num_ids, cod=False, selling_price__range=(price[0],price[1]))

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		query3 = query & query2

		mainNumbers = Numbers.objects.filter(query)
		mainNumbers1 = Numbers.objects.filter(query3)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if start and sum_in_url and cod:
		query = Q()
		query1 = Q(id__in=num_ids, cod=True, number_sum=sum_in_url)
		query2 = Q(id__in=num_ids, cod=False, number_sum=sum_in_url)

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		query3 = query & query2

		mainNumbers = Numbers.objects.filter(query)
		mainNumbers1 = Numbers.objects.filter(query3)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if start and total_in_url and cod:
		query = Q()
		query1 = Q(id__in=num_ids, cod=True, number_total=total_in_url)
		query2 = Q(id__in=num_ids, cod=False, number_total=total_in_url)

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		query3 = query & query2

		mainNumbers = Numbers.objects.filter(query)
		mainNumbers1 = Numbers.objects.filter(query3)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if start and price and sum_in_url:
		query1 = Q(id__in=num_ids, number_sum=sum_in_url, selling_price__range=(price[0],price[1]))
		query = Q()
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		mainNumbers = Numbers.objects.filter(query)


	# mainNumbers = mainNumbers.filter(Q(number_total=total_in_url)| Q(number_sum=sum_in_url))

	if start and total_in_url and sum_in_url:
		query = Q()
		query1 = Q(id__in=num_ids)
		query2 = Q(number_total=total_in_url)
		query3 = Q(number_sum=sum_in_url)
		query2 = query2 | query3

		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1 & query2
		mainNumbers = Numbers.objects.filter(query)


	if sort_order and price and total_in_url:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									number_total=total_in_url, 
									selling_price__range=(price[0],price[1])
									)	

	if sort_order and price and cod:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									cod=True, 
									selling_price__range=(price[0],price[1])
									)
		mainNumbers1 = numbers.filter(
									cod=False, 
									selling_price__range=(price[0],price[1])
									)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if sort_order and total_in_url and cod:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									cod=True, 
									number_total=total_in_url
									)
		mainNumbers1 = numbers.filter(
									cod=False, 
									number_total=total_in_url
									)
		mainNumbers = chain(mainNumbers, mainNumbers1)


	if sort_order and sum_in_url and cod:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									cod=True, 
									number_sum=sum_in_url
									)
		mainNumbers1 = numbers.filter(
									cod=False, 
									number_sum=sum_in_url
									)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if sort_order and price and sum_in_url:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									number_sum=sum_in_url, 
									selling_price__range=(price[0],price[1])
									)	

	if sort_order and total_in_url and sum_in_url:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(Q(number_total=total_in_url)| Q(number_sum=sum_in_url))
	return mainNumbers

	if sort_order and start and cod:
		numbers  = sort_by_order(sort_order,num_ids)

		query = Q()
		query1 = Q(cod=True)
		query2 = Q(cod=False)
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query_cod_true = query & query1
		query_cod_false= query & query2

		mainNumbers = Numbers.objects.filter(query_cod_true)
		mainNumbers1 = Numbers.objects.filter(query_cod_false)
		mainNumbers = chain(mainNumbers, mainNumbers1)	

	if sort_order and total_in_url and cod:
		numbers  = sort_by_order(sort_order,num_ids)
		query_cod_true = Q(cod=True,number_total=total_in_url)
		query_cod_false = Q(cod=False,number_total=total_in_url)

		mainNumbers = Numbers.objects.filter(query_cod_true)
		mainNumbers1 = Numbers.objects.filter(query_cod_false)
		mainNumbers = chain(mainNumbers, mainNumbers1)	

	if sort_order and sum_in_url and cod:
		numbers  = sort_by_order(sort_order,num_ids)
		query_cod_true = Q(cod=True,number_sum=sum_in_url)
		query_cod_false = Q(cod=False,number_sum=sum_in_url)

		mainNumbers = Numbers.objects.filter(query_cod_true)
		mainNumbers1 = Numbers.objects.filter(query_cod_false)
		mainNumbers = chain(mainNumbers, mainNumbers1)	

	if sort_order and price and cod:
		numbers  = sort_by_order(sort_order,num_ids)
		query_cod_true = Q(cod=True,selling_price__range=(price[0],price[1]))
		query_cod_false = Q(cod=False,selling_price__range=(price[0],price[1]))

		mainNumbers = Numbers.objects.filter(query_cod_true)
		mainNumbers1 = Numbers.objects.filter(query_cod_false)
		mainNumbers = chain(mainNumbers, mainNumbers1)

""" Function Ends"""

"""
Method:             sort_number_level_four
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def sort_number_level_four(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod):
	mainNumbers = []
	if start and price and total_in_url and sum_in_url:
		query = Q()
		query1 = Q(id__in=num_ids, selling_price__range=(price[0],price[1]))
		query2 = Q(number_total=total_in_url)
		query3 = Q(number_sum=sum_in_url)
		query2 = query2 | query3
		
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query = query & query1
		query = query & query2
		mainNumbers = Numbers.objects.filter(query)

	# Filter with COD StART 
	if start and cod and total_in_url and price:
		query = Q()
		query_cod_true = Q(id__in=num_ids, cod=True, number_total=total_in_url, selling_price__range=(price[0],price[1]))
		query_cod_false = Q(id__in=num_ids, cod=False,number_total=total_in_url, selling_price__range=(price[0],price[1]))
		
		mainNumbers = Numbers.objects.filter(query_cod_true)
		mainNumbers1 = Numbers.objects.filter(query_cod_false)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if start and cod and sum_in_url and price:
		query = Q()
		query_cod_true = Q(id__in=num_ids, cod=True, number_sum=sum_in_url, selling_price__range=(price[0],price[1]))
		query_cod_false = Q(id__in=num_ids, cod=False, number_sum=sum_in_url, selling_price__range=(price[0],price[1]))
		
		mainNumbers = Numbers.objects.filter(query_cod_true)
		mainNumbers1 = Numbers.objects.filter(query_cod_false)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if start and cod and total_in_url and sum_in_url:
		query = Q()
		query1 = Q(id__in=num_ids, cod=True)
		query11 = Q(id__in=num_ids, cod=False)
		query2 = Q(number_total=total_in_url)
		query3 = Q(number_sum=sum_in_url)
		query2 = query2 | query3
		
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)

		query_cod_true = query & query1 & query2
		query_cod_false = query & query11 & query2

		mainNumbers = Numbers.objects.filter(query_cod_true)
		mainNumbers1 = Numbers.objects.filter(query_cod_false)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if sort_order and cod and total_in_url and sum_in_url:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									number_total=total_in_url, 
									number_sum=sum_in_url, 
									cod=True
									)
		mainNumbers1 = numbers.filter(
									number_total=total_in_url, 
									number_sum=sum_in_url, 
									cod=False
									)
		mainNumbers = chain(mainNumbers, mainNumbers1)
	
	if sort_order and cod and total_in_url and price:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									number_total=total_in_url, 
									selling_price__range=(price[0],price[1]), 
									cod=True
									)
		mainNumbers1 = numbers.filter(
									number_total=total_in_url, 
									selling_price__range=(price[0],price[1]), 
									cod=False
									)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if sort_order and cod and sum_in_url and price:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									number_sum=sum_in_url, 
									selling_price__range=(price[0],price[1]), 
									cod=True
									)
		mainNumbers1 = numbers.filter(
									number_sum=sum_in_url, 
									selling_price__range=(price[0],price[1]), 
									cod=False
									)
		mainNumbers = chain(mainNumbers, mainNumbers1)

	if sort_order and price and total_in_url and sum_in_url:
		numbers  = sort_by_order(sort_order,num_ids)
		mainNumbers = numbers.filter(
									number_total=total_in_url, 
									number_sum=sum_in_url, 
									selling_price__range=(price[0],price[1])
									)

	if sort_order and start and total_in_url and sum_in_url:
		numbers  = sort_by_order(sort_order,num_ids)
		numbers = numbers.filter(Q(number_total=total_in_url) | Q(number_sum=sum_in_url))
		query = Q()
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)
		mainNumbers = numbers.filter(query)

	if sort_order and start and price and sum_in_url:
		numbers  = sort_by_order(sort_order,num_ids)
		print("hello")
		query1 = Q(selling_price__range=(price[0],price[1]), number_sum=sum_in_url)
		query = Q()
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)
		query = query & query1
		mainNumbers = numbers.filter(query)

	if sort_order and start and price and total_in_url:
		# TODO
		numbers  = sort_by_order(sort_order,num_ids)
		query1 = Q(selling_price__range=(price[0],price[1]), number_total=total_in_url)
		query = Q()
		for num in start:
		    query = query | Q(number_for_search__istartswith=num)
		query = query & query1
		mainNumbers = numbers.filter(query)
	return mainNumbers
""" Function Ends"""

"""
Method:             sort_numbers_by_filter
Developer:          Anoop Kumar
Created Date:       04-03-2020
Purpose:            Get Number Details
Params:             number id
Return:             [number]
"""
def sort_numbers_by_filter(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, isAll, cod=None, matchNumbers=None):
	print("\n*************  sort_numbers_by_filter *******************")
	print("Tags >> ", tags)
	
	print("cod >> ", cod)


	cat_numbers = []
	mainNumbers = []
	from riwaz.base.filters import filter_numbers_qs
	if not num_ids:
		matchNumbers = filter_numbers_qs(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod, matchNumbers)
	
	else:

		if len(url_match) == 1:
			print("\n***********>>>>    level 1 ")
			mainNumbers = sort_number_level_one(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod, matchNumbers)

		if len(url_match) == 2:
			print("\n***********>>>>    level 2")
			mainNumbers = sort_number_level_two(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod)

		if len(url_match) == 3:
			print("\n***********>>>>    level 3")
			mainNumbers = sort_number_level_three(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod)

		if len(url_match) == 4:
			print("\n***********>>>>    level 4")
			mainNumbers = sort_number_level_four(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod)

		if len(url_match) == 5:
			print("\n***********>>>>    level 5")
			if sort_order and start and price and total_in_url and sum_in_url:
				numbers  = sort_by_order(sort_order,num_ids)
				mainNumbers = Numbers.objects.filter(
											number_total=total_in_url,
											number_sum=sum_in_url,
											number_for_search__istartswith=start,
											selling_price__range=(price[0],price[1])
											)
		matchNumbers = mainNumbers
		#Total , sum and price is passed
		# if total_in_url and sum_in_url and price:
		# 	mainNumbers = Numbers.objects.filter(
		# 										id__in=num_ids,
		# 										number_total=total_in_url,
		# 										number_sum=sum_in_url,
		# 						# if len(url_match) == 1:
		# 	print("\n***********>>>>    level 1 ")
		# 	mainNumbers = sort_number_level_one(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod, matchNumbers)
		#
		# if len(url_match) == 2:
		# 	print("\n***********>>>>    level 2")
		# 	mainNumbers = sort_number_level_two(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod)
		#
		# if len(url_match) == 3:
		# 	print("\n***********>>>>    level 3")
		# 	mainNumbers = sort_number_level_three(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod)
		#
		# if len(url_match) == 4:
		# 	print("\n***********>>>>    level 4")
		# 	mainNumbers = sort_number_level_four(request, url_match, num_ids, my_wishlist_numbers, sort_order, total_in_url, sum_in_url, price, start, tags, cod)
		#
		# if len(url_match) == 5:
		# 	print("\n***********>>>>    level 5")
		# 	if sort_order and start and price and total_in_url and sum_in_url:
		# 		numbers  = sort_by_order(sort_order,num_ids)
		# 		mainNumbers = Numbers.objects.filter(
		# 									number_total=total_in_url,
		# 									number_sum=sum_in_url,
		# 									number_for_search__istartswith=start,
		# 									selling_price__range=(price[0],price[1])
		# 									)
		# 					number_sum__range=(price[0],price[1])
		# 										)

	# if total_in_url and sum_in_url and price and sort_order:
	# 	# TODO
	# 	print("All cases together")
	
	if matchNumbers.exists():
		if isAll:	
			# print("mainNumber    ")
			# print(mainNumber)
			# if basic:
			# 	num_data = {}
			# 	num_data['isWishlist'] = False
			# 	if mainNumber.display_number in my_wishlist_numbers:
			# 		num_data['isWishlist'] = True

			# 	num_data['id'] = mainNumber.id
			# 	num_data['display_number'] = mainNumber.display_number
			# 	num_data['purchase_price'] = mainNumber.purchase_price
			# 	num_data['total_views'] = mainNumber.total_views
			# 	num_data['total_likes'] = mainNumber.total_likes
			# 	num_data['total_sum'] = mainNumber.number_total
			# 	num_data['end_sum'] = mainNumber.number_sum
			# 	num_data['rtp'] = mainNumber.rtp
				
			# 	if mainNumber.user.is_premium:
			# 		num_data['premium'] = True
			# 	else:
			# 		num_data['premium'] = False

			# 	num_data['tag_premium'] = mainNumber.user.premium_seller_tag
			# 	cat_numbers.append(num_data)
			# 	# print("---------->>>>>>>>>>>> ")

			for mainNumber in matchNumbers:
				print(" Im all number" , mainNumber)
				if mainNumber.user.is_active:
					if str(mainNumber.number_status) == str(1):
						# if mainNumber.user.is_premium:
						num_data = {}
						num_data['isWishlist'] = False
						if mainNumber.display_number in my_wishlist_numbers:
							num_data['isWishlist'] = True

						num_data['id'] = mainNumber.id
						num_data['display_number'] = mainNumber.display_number
						num_data['purchase_price'] = mainNumber.selling_price
						num_data['total_views'] = mainNumber.total_views
						num_data['total_likes'] = mainNumber.total_likes
						num_data['total_sum'] = mainNumber.number_total
						num_data['end_sum'] = mainNumber.number_sum
						num_data['rtp'] = mainNumber.rtp
						num_data['rating'] = mainNumber.user.seller_rating
						if mainNumber.user.is_premium:
							num_data['premium'] = True
						else:
							num_data['premium'] = False

						num_data['tag_premium'] = mainNumber.user.premium_seller_tag
						cat_numbers.append(num_data)
		else:
			for mainNumber in matchNumbers:
				# print("meamel")
				print(" not isAll number")
				if mainNumber.user.is_active and mainNumber.user.is_premium and str(mainNumber.number_status) == str(1):
					num_data = {}
					num_data['isWishlist'] = False
					if mainNumber.display_number in my_wishlist_numbers:
						num_data['isWishlist'] = True

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
					if mainNumber.user.is_premium:
						num_data['premium'] = True
					else:
						num_data['premium'] = False

					cat_numbers.append(num_data)
	return cat_numbers

""" Function Ends"""