from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from riwaz.users.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from riwaz.category.models import RiwazCategory
from riwaz.menu.models import RiwazMenu

# from models import User
import json
import datetime
import math, random 
import requests
from django.conf import settings

BASE_DIR = settings.MEDIA_ROOT

"""
Method:             home
Developer:          Anoop Kumar
Created Date:       24-03-2020
Purpose:            Home
Params:             null
Return:             null
"""
def home(request):
	# if 'cart_data' in request.session:
	# 	cartVal = request.session['cart_data']
	# else:
	# 	cartVal = []
	# getHomeImages = Homeimages.objects.filter(status = True).all()
	# testimonials = Testimonials.objects.all().values('rating_stars', 'testimonial', 'name', 'review_on', 'review_url')
	menus = RiwazMenu.objects.order_by('?')[0:3]
	
	return render(request, 'home/index.html', {'menus':menus,'spices':spices})
"""end function dashboard"""

