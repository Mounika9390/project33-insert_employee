from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_employee(request):
    EEFO=EmployeeForm()
    d={'EEFO':EEFO}
    if request.method=='POST':
        EDFO=EmployeeForm(request.POST)
        if EDFO.is_valid():
            en=EDFO.cleaned_data['ename']
            dn=EDFO.cleaned_data['deptno']
            j=EDFO.cleaned_data['job']
            EO=Employee.objects.get_or_create(ename=en,deptno=dn,job=j)[0]
            EO.save()
            return HttpResponse('insert_employee is valid')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_employee.html',d)

def insert_dept(request):
    EDFO=DeptForm()
    d={'EDFO':EDFO}
    if request.method=='POST':
        DDFO=DeptForm(request.POST)
        if DDFO.is_valid():
            dn=DDFO.cleaned_data['deptno']
            EO=Employee.objects.get(deptno=dn)
            dn=DDFO.cleaned_data['dname']
            dl=DDFO.cleaned_data['dloc']
            DEO=Dept.objects.get_or_create(deptno=EO,dname=dn,dloc=dl)[0]
            DEO.save()
            return HttpResponse('insert_dept is valid')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_dept.html',d)