from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
# from users import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]