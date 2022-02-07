from django.core.validators import MinValueValidator
from django.db import models

from user.models.human import Human
from utility.validators import validate_typed_foreign_key


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, Human, Human.EMPLOYEE)


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
