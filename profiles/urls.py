from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<str:pk>/', views.user_profile, name='profile'),
]