from django.core.exceptions import ValidationError
from django.db import models

from account.models.customerAccount import CustomerAccount
from user.models import Employee
from account.models import Account


class ConversionTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = None
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True
        unique_together = ['account_id', 'date']


class TypeConversionTransaction(ConversionTransaction):
    account_id = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        try:
            self.__class__.objects.get(pk=self.id)
        except:
            try:
                num_of_conversions = len(self.__class__.objects.get(account_id=self.account_id.acc_id))
                account = self.account_id

                # state = False
                if num_of_conversions % 2 == 0:
                    if account.type != CustomerAccount.PROFITING:
                        raise ValidationError(f"transaction hasn't been applied")
                else:
                    if account.type != CustomerAccount.REGULAR:
                        raise ValidationError(f"transaction hasn't been applied")
            except:
                account = self.account_id
                # state = False
                if account.type != CustomerAccount.PROFITING:
                    raise ValidationError(f"transaction hasn't been applied")


def validate_employee_on_change_account(employee_id):
    the_employee = Employee.objects.get(pk=employee_id)
    if not (the_employee.status and the_employee.can_block_account):
        raise ValidationError(f"the employee must be on work and be able to block account")


class StateConversionTransaction(ConversionTransaction):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, validators=[
        validate_employee_on_change_account
    ])

    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        try:
            self.__class__.objects.get(pk=self.id)
        except:
            try:
                num_of_conversions = len(self.__class__.objects.get(account_id=self.account_id.acc_id))
                account = self.account_id
                # state = False
                if num_of_conversions % 2 == 0:
                    if account.state != account.CLOSED:
                        raise ValidationError(f"transaction hasn't been applied")
                else:
                    if account.state != account.OPEN:
                        raise ValidationError(f"transaction hasn't been applied")
            except:
                # print('jesus', self.account_id)
                # account = Account.objects.get(pk=self.account_id)
                account = self.account_id
                # state = False
                if account.state != account.CLOSED:
                    raise ValidationError(f"transaction hasn't been applied")

    # constraint: Account.state = count(ChangeAccountTransaction) % 2 == 0
