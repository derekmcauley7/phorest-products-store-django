from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': "form-control",'style': 'max-width: 300px;', 'placeholder':'email'}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': "form-control",'style': 'max-width: 300px;', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': "form-control",'style': 'max-width: 300px;', 'placeholder':'password'}),
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name",  "username", "email", "password1", "password2"]
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
                }),
        }