from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Human)
admin.site.register(HumanName)
admin.site.register(HumanAddress)
admin.site.register(HumanPhoneNumber)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(EmployeeWorkingHours)

