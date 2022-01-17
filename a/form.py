from django import forms
from django.contrib.auth.models import User

class SignUpform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

class Student(forms.Form):
    class Meta:
        fields = ['name', 'address']