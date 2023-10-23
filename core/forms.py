from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'form-control w-70  rounded-lg', 
        'id':'uname',
    }))   
    
    password =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your Password',
        'class': 'form-control w-70  rounded-lg', 
        'id':'pw',
    }))   

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'form-control w-70  rounded-lg', 
        'id':'uname',
    }))   
    email =  forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'form-control w-70  rounded-lg', 
        'id':'mail',
    }))   
    password1 =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your Password',
        'class': 'form-control w-70  rounded-lg', 
        'id':'pw1',
    }))   
    password2 =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Re-Enter Your Password',
        'class': 'form-control w-70  rounded-lg', 
        'id':'pw2',
    }))   

