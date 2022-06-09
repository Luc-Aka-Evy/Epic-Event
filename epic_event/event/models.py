import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):

    name =models.CharField(max_length=128)
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    type = models.CharField(max_length=50)


class Contract(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(null=True)
    signed = models.BooleanField(default=False)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="seller"
    )


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    adress = models.CharField(max_length=255, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(null=True)
    support = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="support"
    )


class CompanyEvents(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)