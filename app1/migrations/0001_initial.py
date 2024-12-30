# Generated by Django 5.0.4 on 2024-12-20 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Dept_name', models.CharField(max_length=100)),
                ('Loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Emp_name', models.CharField(max_length=100)),
                ('Job', models.CharField(max_length=100)),
                ('Mgr', models.IntegerField()),
                ('Hiredate', models.DateField()),
                ('Salary', models.IntegerField()),
                ('Commission', models.IntegerField()),
                ('Dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
            ],
        ),
    ]
