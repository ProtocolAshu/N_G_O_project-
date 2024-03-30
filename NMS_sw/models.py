from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 #models.py


class inventory(models.Model):
    sclass=models.PositiveIntegerField(null=True)
    books=models.PositiveIntegerField(null=True)
    uniforms=models.PositiveIntegerField(null=True)

class Admin(models.Model):
    username=models.CharField(max_length=120,null=True)
    password=models.CharField(max_length=120,null=True)
class estimations(models.Model):
    sclass=models.PositiveIntegerField(null=True)
    books=models.PositiveIntegerField(null=True)
    uniforms=models.PositiveIntegerField(null=True)

class totalmoney(models.Model):
    Sum=models.PositiveIntegerField("money",null=True)
    
# class renewal(models.Model):
#     session=models.PositiveIntegerField(null=True)
    
class expenditure(models.Model):
    exp=models.PositiveIntegerField(null=True)
    
class exphist(models.Model):
    expe=models.PositiveIntegerField(null=True)
    rec=models.CharField(max_length=801,null=True)

class register_Donor(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Number = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

# class Renewal(models.Model):
#     File_name=models.FileField(upload_to='performance')

class Donor_avail(models.Model):
    money=models.PositiveBigIntegerField("Rupees",null=True)
    donor=models.ForeignKey(register_Donor,null=True,on_delete=models.CASCADE)
    status=models.BooleanField(null=True)
    ubstatus=models.BooleanField(null=True)
    time=models.DateTimeField(null=True)
    lastpaid=models.DateTimeField(null=True)
    # address = models.CharField(max_length=100)
    #frequency
    frequency=models.CharField(max_length=120,null=True)
    books=models.PositiveSmallIntegerField(null=True)
    uniform=models.PositiveSmallIntegerField(null=True)#stores class


class Student(models.Model):
    fullName = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    Grade= models.CharField(max_length=100)
    schoolName = models.CharField(max_length=100)
    money_needed=models.PositiveIntegerField(null=True)
    books=models.BooleanField(null=True,default=False)
    uniform=models.BooleanField(null=True, default=False)
    performance=models.FloatField(null=True)
    guardianName = models.CharField(max_length=100)
    score=models.FloatField(null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2)

    def __score__(self):
        income_coeff=0.5
        income_limit=500000.0
        gender_flag = 0
        performance_coeff=0.37
        gender_coefficient=1-income_coeff-performance_coeff
        if(self.gender=="Female"):
            gender_flag=1
        
        new_score = income_coeff*(income_limit-int(self.income))/income_limit+performance_coeff*float(self.performance)/100+gender_coefficient*gender_flag/2
        self.score = float(new_score)

