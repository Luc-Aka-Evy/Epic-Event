import email
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Company(models.Model):

    name = models.CharField(max_length=128)
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Contract(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    signed = models.BooleanField(default=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")


class Event(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048)
    date = models.DateField(null=True)
    adress = models.CharField(max_length=255, default="")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    support = models.ForeignKey(User, on_delete=models.CASCADE, related_name="support")