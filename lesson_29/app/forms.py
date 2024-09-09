from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm




class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2', 'cv', 'photo', 'id_photo')





