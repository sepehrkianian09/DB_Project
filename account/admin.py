from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Account)
admin.site.register(BankAccount)
admin.site.register(CustomerAccount)
admin.site.register(RegularAccount)
admin.site.register(TypeConversionTransaction)
admin.site.register(StateConversionTransaction)
