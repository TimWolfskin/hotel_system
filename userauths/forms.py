from django import forms
from django.contrib.auth.forms import UserCreationForm

from userauths.models import User, Profile



class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TimeInput(attrs={'placeholder':"Enter Full Name", 'class':"a custom class"}))
    username = forms.CharField(widget=forms.TimeInput(attrs={'placeholder':"Username", 'class':"a custom class"}))
    email = forms.EmailField(widget=forms.TimeInput(attrs={'placeholder':"Email Address", 'class':"a custom class"}))
    phone = forms.CharField(widget=forms.TimeInput(attrs={'placeholder':"Phone Number", 'class':"a custom class"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Password", 'class':"a custom class"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Confirm Password", 'class':"a custom class"}))



    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone', 'password1', 'password2']