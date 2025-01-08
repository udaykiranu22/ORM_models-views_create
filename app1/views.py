from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *
from django.db.models.functions import Length

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

def select_related1(request):
    data1 = Employee.objects.all().select_related('Dept_no')
    data1 = Employee.objects.select_related('Dept_no').filter(Emp_no='1')
    data1 = Employee.objects.select_related('Dept_no').filter(Emp_no__range=(3,6))
    data1 = Employee.objects.select_related('Dept_no').filter(Emp_name__contains='u')
    data1 = Employee.objects.select_related('Dept_no').filter(Emp_name__startswith='c')
    data1 = Employee.objects.select_related('Dept_no').filter(Emp_name__endswith='n')
    data1 = Employee.objects.select_related('Dept_no').filter(Emp_name__regex='^\wh+')
    data1 = Employee.objects.select_related('Dept_no').filter(Emp_no__in=(2,5))
    data1 = Employee.objects.select_related('Dept_no').all()[1:7:2]
    data1 = Employee.objects.select_related('Dept_no').all().order_by('Emp_name')
    data1 = Employee.objects.select_related('Dept_no').all().order_by('-Emp_name')
    data1 = Employee.objects.select_related('Dept_no').all().order_by(Length("Emp_name"))
    data1 = Employee.objects.select_related('Dept_no').all().order_by(Length("Emp_name").desc())
    data1 = Employee.objects.select_related('Dept_no').filter(Salary__gt = '10000')
    data1 = Employee.objects.select_related('Dept_no').filter(Salary__lt = '20000')
    data1 = Employee.objects.select_related('Dept_no').filter(Salary__gte = '100000')
    data1 = Employee.objects.select_related('Dept_no').filter(Salary__lte = '10000')
    data1 = Employee.objects.select_related('Dept_no').exclude(Emp_no='1')
    data1 = Employee.objects.select_related('Dept_no').filter(Commission__isnull=True)
    data1 = Employee.objects.select_related('Dept_no').filter(Commission__isnull=False)
    data1 = Employee.objects.select_related('Dept_no').filter(Dept_no__Loc='bangalore')
    d = {'data1':data1}
    return render(request, 'select_related.html', d)

def select_related_mgr(request):
    data1 = Employee.objects.all().select_related('Mgr')
    data1 = Employee.objects.select_related('Mgr').all()[1:7:2]
    data1 = Employee.objects.select_related('Mgr').filter(Mgr='1')
    data1 = Employee.objects.select_related('Mgr').filter(Commission__isnull=True)
    data1 = Employee.objects.select_related('Mgr').filter(Commission__isnull=False)
    data1 = Employee.objects.select_related('Mgr').filter(Mgr__Salary__gt='10000')
    data1 = Employee.objects.select_related('Mgr').filter(Mgr__Salary__lt='100000')
    data1 = Employee.objects.select_related('Mgr').filter(Mgr__Salary__gte='100000')
    data1 = Employee.objects.select_related('Mgr').filter(Mgr__Salary__lte='100000')
    data1 = Employee.objects.select_related('Mgr').filter(Mgr__Commission__isnull=True)
    data1 = Employee.objects.select_related('Mgr').filter(Mgr__Commission__isnull=False)
    data1 = Employee.objects.select_related('Mgr').filter(Mgr__Job='python developer')
    d = {'data1':data1}
    return render(request, 'select_related_mgr.html', d)

def multiple_tables(request):
    data1 = Employee.objects.all().select_related('Dept_no','Mgr')
    data1 = Employee.objects.select_related('Dept_no','Mgr').filter(Mgr='1')
    data1 = Employee.objects.select_related('Dept_no','Mgr').filter(Commission__isnull=True)
    data1 = Employee.objects.select_related('Dept_no','Mgr').filter(Commission__isnull=False)
    d = {'data1': data1}
    return render(request, 'multiple_tables.html', d)

def prefetch_related1(request):
    LDEO = Department.objects.prefetch_related('employee_set').all()
    print(LDEO)
    d = {'LDEO':LDEO}
    return render(request, 'prefetch_related1.html', d)