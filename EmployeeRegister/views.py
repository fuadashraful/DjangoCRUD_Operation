# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import Employee_form
from .models import Employee

# Create your views here.

def EmployeeList(request):
    context={
        'employee_list':Employee.objects.all()
    }
    return render(request,'employee_list.html',context)

def EmployeeForm(request,id=0):
    if request.method=="GET":
        if id==0:
            form=Employee_form()
        else:
            employee=Employee.objects.get(pk=id)
            form=Employee_form(instance=employee)
            
        return render(request,'employee_form.html',{"form":form})
    else:
        if id==0:
            form=Employee_form(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=Employee_form(request.POST,instance=employee)

        if form.is_valid():
            form.save()
        return redirect('employeeList')
 
         

def EmployeeDelete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employeeList')