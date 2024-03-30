from django import forms
from .models import Student, Donor_avail
from django.forms import ModelForm

#create a student form 
class Studentform(ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        
        #widgets
class Donor_availform(ModelForm):
    class Meta:
        model=Donor_avail
        fields=('money','books','uniform','frequency')
        