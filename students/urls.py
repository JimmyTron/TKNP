from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='Student'),
    path('profile/', views.profile, name='Profile'), 
] 
