from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'phone_number']
        widgets = {
            'username': forms.TextInput(attrs={"placeholder": "Username"}),
            'phone_number': forms.TextInput(attrs={"placeholder": "Phone number"}),
            'password1': forms.PasswordInput(attrs={"placeholder": "password1"}),
            'password2': forms.PasswordInput(attrs={"placeholder": "password2"})
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Username"}))

    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Phone number"}))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "password"}))
