from django.db import models
from django.contrib.auth.models import User

class User:
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

