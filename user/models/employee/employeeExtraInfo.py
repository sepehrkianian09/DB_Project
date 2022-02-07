import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account.models import Account
from .employee import Employee


class EmployeeWorkingHours(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    working_day = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(6),
    ])
    start_hour = models.TimeField(default=datetime.time())
    end_hour = models.TimeField(default=datetime.time())

    def clean(self):
        super().clean()
        if self.end_hour <= self.start_hour:
            raise ValidationError(f"start_hour should be smaller than end_hour")

    class Meta:
        unique_together = ['employee_id', 'working_day']


def validate_employee_on_change_account(employee_id):
    the_employee = Employee.objects.get(pk=employee_id)
    if not (the_employee.status and the_employee.can_block_account):
        raise ValidationError(f"the employee must be on work and be able to block account")


class EmployeeChangeAccountTransaction(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, validators=[
        validate_employee_on_change_account
    ])
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    # constraint: Account.state = count(ChangeAccountTransaction) % 2 == 0

    class Meta:
        unique_together = ['account_id', 'date']
