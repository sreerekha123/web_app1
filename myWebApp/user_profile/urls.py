from django.urls import path
from .views import login_view, register_view, profile, profile_update, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('/logout/', logout_view, name='logout'),
    path('', register_view, name='register'),
    path('/profile/', profile, name='profile'),
    path('/profile/update/', profile_update, name='profile_update'),
]