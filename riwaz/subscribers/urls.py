from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
# from users import views

urlpatterns = [
	url(r'subscribe/$', views.subscribe, name='subscribe'),
]
