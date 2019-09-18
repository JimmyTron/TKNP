from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('clearance/', views.clearance, name='Clearance'),
     path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='students-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='students/logout.html'), name='logout'),
]