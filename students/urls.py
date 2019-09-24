from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='Student'),
    path('docs/', views.docs, name='Documentation'),
    path('profile/', views.profile, name='Profile'), 
    path('register/', views.register, name='students-registration'),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='students-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='students/logout.html'), name='logout'),
] 
