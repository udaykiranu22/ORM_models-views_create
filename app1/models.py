from django.db import models

# Create your models here.


class Department(models.Model):
    Dept_no = models.IntegerField(primary_key=True)
    Dept_name = models.CharField(max_length=100)
    Loc = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Dept_no)

class Employee(models.Model):
    Emp_no = models.IntegerField(primary_key=True)
    Emp_name = models.CharField(max_length=100)
    Job = models.CharField(max_length=100)
    Mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    Hiredate = models.DateField(auto_now=True)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Commission = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Dept_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Emp_no)


