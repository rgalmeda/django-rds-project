from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# 4example creating form from model
# from books.models import Book

class SignupForm(UserCreationForm):
    class Meta: # telling model to override
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        # widgets ={
        #     'username':forms.TextInput(attrs={'class'})
        # }
