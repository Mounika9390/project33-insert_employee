from django import forms
from app.models import *

class EmployeeForm(forms.Form):
    ename=forms.CharField()
    deptno=forms.IntegerField()
    job=forms.CharField()

class DeptForm(forms.Form):
    el=[[eo.deptno,eo.deptno] for eo in Employee.objects.all()]
    deptno=forms.ChoiceField(choices=el)
    dname=forms.CharField()
    dloc=forms.CharField()