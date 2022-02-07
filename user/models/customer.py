from django.core.exceptions import ValidationError
from django.db import models

from .human import Human


def validate_id(employee_id):
    if Human.objects.get(pk=employee_id).type != Human.CUSTOMER:
        raise ValidationError(
            f'{employee_id}s is not an Employee Instance'
        )


class Customer(models.Model):
    employee_id = models.ForeignKey(Human, on_delete=models.CASCADE, validators=[
        validate_id
    ], primary_key=True)
