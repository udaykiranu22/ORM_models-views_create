from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *

def insert_dept(request):
    dno = int(input("Enter Department Number: "))
    dname = input("Enter Department Name: ")
    loc = input("Enter Location: ")
    do = Department.objects.get_or_create(Dept_no=dno, Dept_name=dname, Loc=loc)
    if do[1]:
        data = Department.objects.all()
        d = {'data':data}
        return render(request, 'display_dept.html', d)
    else:
        return HttpResponse(f"{dname} Department Already Exists")

def insert_emp(request):
    eno = int(input("Enter Employee Number: "))
    ename = input("Enter Employee Name: ")
    job = input("Enter Job: ")
    mgr = input("Enter Manager Number: ")
    if mgr:
        int(mgr)
        mgro = Employee.objects.filter(Emp_no=mgr)
    else:
        mgro = None
    hiredate = input("Enter Hiredate: ")
    sal = float(input("Enter Salary: "))
    comm = input("Enter Commission: ")
    if comm:
        float(comm)
    else:
        comm = None
    deptno = int(input("Enter Department Number: "))
    dno = Department.objects.filter(Dept_no=deptno)
    if dno[0]:
        do = Employee.objects.get_or_create(Emp_no=eno, Emp_name=ename, Job=job, Mgr=mgro, Hiredate=hiredate, Salary=sal, Commission=comm, Dept_no=dno[0])
        if do[1]:
            data1 = Employee.objects.all()
            d = {'data1':data1}
            return render(request, 'display_emp.html', d)
        else:
            return HttpResponse(f"{ename} Employee data Already Exists")
    else:
        return HttpResponse(f"{deptno} this department number doesn't exist")

def display_dept(request):
    data = Department.objects.all()
    d = {'data':data}
    return render(request, 'display_dept.html', d)

def display_emp(request):
    data1 = Employee.objects.all()
    d = {'data1':data1}
    return render(request, 'display_emp.html', d)