from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Resume(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    grade = models.CharField(max_length=40)
    speciality = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    education = models.CharField(max_length=300)
    experience = models.TextField()
    portfolio = models.TextField()
    title = models.CharField(max_length=60)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField()
