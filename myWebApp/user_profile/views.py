from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm, UserRegistrationForm, UserProfileUpdateForm

@login_required
def profile(request):
    user = request.user
    print('name :',user)
    return render(request, 'user_profile/profile.html', {'user': user})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'user_profile/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect('register')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user_profile/register.html', {'form': form})

@login_required
def profile_update(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=user_profile)

    return render(request, 'user_profile/profile_update.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')