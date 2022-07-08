from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def addNewSample(request):
    sample = Sample(sample_id='IDX', model_code='CODE', subcategory = 'TV PANEL', working_condition=True)
    sample.save()

def addNewEmployee(request):
    employee =employee(name='IDX', emp_id='CODE')
    employee.save()

def searchSample(request):
    field_name = "xyz"
    toCheck = "ab"
    field_name_icontains = field_name+'__icontains'
    queryset = Sample.objects.filter(**{field_name_icontains: toCheck})