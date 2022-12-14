from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms
from .forms import RegisterForm
from .models import Profile

COUNTRIES = (
    ('ireland','Ireland'),
    ('england', 'England'),
    ('poland','Poland'),
    ('germany','Germany'),
    ('france','France'),
)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            return render(response, "profile/register.html", {"form":form}) 
    else:
        form = RegisterForm()
        return render(response, "profile/register.html", {"form":form})

class LogoutInterfaceView(LogoutView):
    template_name = 'profile/logout.html'
    success_url = 'products'

class LoginInterfaceView(LoginView):
    template_name = 'profile/login.html'
    success_url = 'profile'

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, min_length=2)
    last_name = forms.CharField(required=True, min_length=2)
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
class UserProfileForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    post_code = forms.CharField(required=True)
    country = forms.CharField(widget=forms.Select(choices=COUNTRIES), required=True)
    class Meta:
        model = Profile
        fields = ("address_1", "address_2", "country", "post_code")

@login_required()
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("products")
        else:
            return render(request, "profile/profile.html", {"u_form":user_form, "p_form": user_profile_form})
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, "profile/profile.html", {"u_form":user_form, "p_form": user_profile_form})