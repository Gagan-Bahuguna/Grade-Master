from django.forms import forms
from django import forms
class UsersForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
    num3=forms.CharField()