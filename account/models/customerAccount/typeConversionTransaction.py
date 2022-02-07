from django.core.exceptions import ValidationError
from django.db import models

from .customerAccount import CustomerAccount
from user.models import Employee
from .. import Account


class TypeConversionTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    customer_acc_id = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    conversion_date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ['customer_acc_id', 'conversion_date']


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
