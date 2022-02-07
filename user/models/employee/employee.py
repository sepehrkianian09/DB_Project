from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, BaseValidator
from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _, ngettext_lazy

from user.models.human import Human


def validate_id(employee_id):
    if Human.objects.get(pk=employee_id).type != Human.EMPLOYEE:
        raise ValidationError(
            _('%(value)s is not an Employee Instance'),
            params={'value': employee_id},
        )


class Employee(models.Model):
    employee_id = models.ForeignKey(Human, on_delete=models.CASCADE, validators=[
        validate_id
    ], primary_key=True)

    ON_WORK = 'O'
    FIRED = 'F'
    STATUS_CHOICES = ((ON_WORK, 'employee'), (FIRED, 'Customer'))
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=ON_WORK
    )

    monthly_salary = models.BigIntegerField(
        validators=[
            MinValueValidator(0)
        ],
        default=0
    )

    can_block_account = models.BooleanField(default=False)