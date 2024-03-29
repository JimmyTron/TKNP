from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Request

class ClearanceRequestForm(forms.ModelForm):
    departments = forms.MultipleChoiceField

    class Meta:
        model = Request
        fields = ['student', 'request','date_posted','status']

class RequestForm(forms.ModelForm):
    departments = forms.MultipleChoiceField
    class Meta:
        model = Request
        fields = ['student', 'request','date_posted', 'status']