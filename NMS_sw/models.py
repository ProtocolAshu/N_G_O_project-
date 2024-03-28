# models.py

from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    class_field = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    performance_card = models.FileField(upload_to='performance_cards/')
    guardian_name = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.CharField(max_length=100)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
