from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Department, Request

class ClearanceRequestForm(forms.ModelForm):
    #departments = forms.MultipleChoiceField
    departments = forms.ModelChoiceField(widget=forms.HiddenInput,queryset=Department.objects.all(),disabled=True)
    student = forms.ModelChoiceField(widget=forms.HiddenInput,queryset=get_user_model,disabled=True)

    class Meta:
        model = Request
        fields = ['student', 'request', 'departments','date_posted']