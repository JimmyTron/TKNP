from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    admission_number = forms.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'admission_number', 'password1','password2']

class StudentUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Profile
        fields = ['department','course','image','Adm_no']

class DepartmentalClearanceForm(object):
    pass        

class ClearanceForm(object):
    pass