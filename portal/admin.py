from django.contrib import admin

# Register your models here.
from .models import Employee, Sample, Ownership

admin.site.register(Employee)
admin.site.register(Ownership)
admin.site.register(Sample)