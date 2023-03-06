from django.db import models

# Create your models here.

class Employee(models.Model):
    sid = models.IntegerField(primary_key=True) #employee number
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    birthday = models.DateField()
    # ifcar = models.BooleanField()  # if has car

class Car(models.Model):
    c_id = models.AutoField(primary_key=True)
    car_number = models.CharField(max_length=20) #car number
    user_id = models.IntegerField() #employee number
    car_brand = models.CharField(max_length=50)
    car_color = models.CharField(max_length=20)
    car_type = models.CharField(max_length=30)

class Records(models.Model):
    '''
    Record car access
    '''
    sid = models.AutoField(primary_key=True)
    enter_time = models.DateField(auto_now_add=True)
    out_time = models.DateField()
    car_number = models.CharField(max_length=20)
    stay_time = models.TimeField()