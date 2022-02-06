from django.core.validators import MinLengthValidator
from django.db import models

from user.models.Human import Human


class Employee(models.Model):
    employee_id = models.ForeignKey(Human, on_delete=models.CASCADE, validators=[
        # todo Human.type = 'E'
    ])

    ON_WORK = 'O'
    FIRED = 'F'
    STATUS_CHOICES = ((ON_WORK, 'Employee'), (FIRED, 'Customer'))
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

