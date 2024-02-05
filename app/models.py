from django.db import models

# Create your models here.

class Employee(models.Model):
    ename=models.CharField(max_length=100,primary_key=True)
    deptno=models.IntegerField()
    job=models.CharField(max_length=100)

class Dept(models.Model):
    deptno=models.ForeignKey(Employee,on_delete=models.CASCADE)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)