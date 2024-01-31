from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    # Custom login form if needed
    pass

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']