from django.core.validators import MinLengthValidator
from django.db import models

from user.models.human import Human


class Employee(models.Model):
    employee_id = models.ForeignKey(Human, on_delete=models.CASCADE, validators=[
        # todo human.type = 'E'
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

