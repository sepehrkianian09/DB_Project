from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .employee import Employee


class EmployeeWorkingHours(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    working_day = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(6),
    ])
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    class Meta:
        unique_together = ['employee_id', 'working_day']


class EmployeeChangeAccountTransaction(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    # account_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    new_state = models.BooleanField
    date = models.DateTimeField()

    # class Meta:
    # unique_together = ['employee_id', 'account_id', 'date']
