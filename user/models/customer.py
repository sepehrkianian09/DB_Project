from django.db import models

from utility.validators import validate_typed_foreign_key
from .human import Human


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, Human, Human.CUSTOMER)


class Customer(models.Model):
    customer_id = models.ForeignKey(Human, on_delete=models.CASCADE, validators=[validate_id], primary_key=True)
