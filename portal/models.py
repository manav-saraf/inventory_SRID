from pyexpat import model
from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=30)
    samples = models.ManyToManyField('Sample', through='Ownership', related_name='employees')


class Sample(models.Model):
    sample_id = models.CharField(max_length=30)
    model_code = models.CharField(max_length=30)
    subcategory = models.CharField(max_length=30)
    working_condition = models.BooleanField()


class Ownership(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    ownership_type = models.TextChoices('OwnershipType', 'PERMANENT TEMPORARY')
