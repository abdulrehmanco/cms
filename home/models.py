from enum import auto
from django.db import models
from cms.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models.fields import TextField
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

# Create your models here.

class Company(models.Model):
    name= models.CharField(max_length=200, null=True)
    id = models.AutoField(primary_key=True)
    contact= models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=200, null=True)
    desc=  models.TextField(max_length=500, null=True)
    added_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name

class Medicine(models.Model):
    id= models.AutoField(primary_key=True)
    company_id= models.ForeignKey(Company , on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=50, null=True)
    sell_price= models.CharField(max_length=200, null=True)
    buy_price= models.CharField(max_length=200, null=True)
    desc= models.CharField(max_length=200, null=True)
    in_stock= models.CharField(max_length=200, null=True)
    added_on= models.DateTimeField(auto_now_add=True)
    shelf_no= models.CharField(max_length=50,null=True)

    def __str__(self):
         return self.name

     



class Employee(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200, null=True)
    contact= models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=200, null=True)
    joining_date= models.DateField()

    def __str__(self):
         return self.name

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.name

class Bill(models.Model):
    id=models.AutoField(primary_key=True)
    medicine_id=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    qty=models.IntegerField()
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return str(self.customer_id)

class EmployeeSalary(models.Model):
    id=models.AutoField(primary_key=True)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary_date=models.DateField()
    salary_amount=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.employee_id