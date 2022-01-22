from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
# User = get_user_model()


class Gamer(models.Model):
    """"defines gamer class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
