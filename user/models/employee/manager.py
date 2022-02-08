from django.db import models

<<<<<<< HEAD:user/models/manager.py
from user.models.Employee import Employee
=======
from user.models.employee import Employee
>>>>>>> 201adfec667192835e91c975b5037b5d85047c44:user/models/employee/manager.py


class Manager(models.Model):
    manager_id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    # bank_account_id = models.ForeignKey(BankAccount, unique=True)
