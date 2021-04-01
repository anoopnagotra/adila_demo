from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from riwaz.subscribers.models import Subscribers
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from pprint import pprint 
import re
from django.db.models import Q

# from models import User
import json
import datetime
import requests
from django.utils.timezone import utc

def subscribe(request):
	if request.method == "POST":
		email = request.POST.get('email',None).strip()
		if Subscribers.objects.filter(email = email).exists():
			messages.warning(request, 'Email is already exist. Try with another email')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			user = Subscribers.objects.create(email = email, category_id='', status=True)
			messages.success(request, 'You have subscribed the news letter successfully')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



