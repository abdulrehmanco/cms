from rest_framework import serializers
from django.db import models
from django.db.models import fields

from home.models import Bill, Company, Customer, Employee, EmployeeSalary, Medicine

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model= Company
        fields=['id','name','contact','address','desc','added_on']

class MedicineSerializers(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields=['id','company_id','name','sell_price','buy_price','desc','in_stock','added_on','shelf_no']

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerializers(instance.company_id).data
        return response


         
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','name','contact','address','joining_date']


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','name','contact','address','added_on']


class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields=['id','medicine_id','customer_id','qty','added_on']

class EmployeeSalarySerializers(serializers.ModelSerializer):
    class Meta:
        model=EmployeeSalary
        fields=['id','employee_id','salary_date','salary_amount','added_on']

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['employee']=EmployeeSerializers(instance.employee_id).data
        return response      


