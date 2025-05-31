from django.contrib.auth.models import AbstractUser
from django.db import models

class Address(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True, default='')
    street = models.CharField(max_length=200, blank=True, null=True, default='')
    home = models.IntegerField(blank=True, null=True, default=0)
    entrance = models.IntegerField(blank=True, null=True, default=0)
    floor = models.IntegerField(blank=True, null=True, default=0)
    apartment = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.home}"

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=17, null=True, blank=True, default='')
    telegram = models.CharField(max_length=32, null=True, blank=True, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True, default=0)
    bio = models.TextField(blank=True, null=True, default='')
