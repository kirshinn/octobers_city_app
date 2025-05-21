from django.contrib.auth.models import AbstractUser
from django.db import models

class Address(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    home = models.IntegerField(blank=True, null=True)
    entrance = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    apartment = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.home}"

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
