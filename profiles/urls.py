from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),

]