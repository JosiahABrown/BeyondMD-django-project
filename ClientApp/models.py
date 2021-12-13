from django.db import models
from twilio.rest import Client

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    
class Clients(models.Model):
    ClientId = models.AutoField(primary_key=True)
    ClientName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
