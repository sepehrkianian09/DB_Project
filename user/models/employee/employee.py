from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models.human import Human


def validate_id(employee_id):
    if Human.objects.get(pk=employee_id).type != Human.EMPLOYEE:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': employee_id},
        )


class Employee(models.Model):
    employee_id = models.ForeignKey(Human, on_delete=models.CASCADE, validators=[
        # todo human.type = 'E'
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
            MinLengthValidator(0)
        ]
    )

    can_block_account = models.BooleanField(default=False)
