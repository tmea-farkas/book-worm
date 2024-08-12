from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<str:pk>/', views.user_profile, name='profile'),
    path('update/profile/', views.profile_update, name='profile-update'),
    path('accounts/profile/', views.profile_redirect, name='user-profile'),
    path('profile/delete/profile/<str:pk>/', views.delete_profile, name='delete-profile'),
]