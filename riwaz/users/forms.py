from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        # fields = ('name', 'email','role','attorney_no','profile_image','age_group','mobile','city','country','address')
        fields = '__all__'

class UserChangeForm(UserChangeForm):
	class Meta:
		model = User
		# fields = ('email',)
		fields = '__all__'
