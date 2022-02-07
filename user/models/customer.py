from django.db import models
from utility.validators import typed_foreign_key_validator_func
from .human import Human


class Customer(models.Model):
    employee_id = models.ForeignKey(Human, on_delete=models.CASCADE, validators=[
        typed_foreign_key_validator_func(Human, Human.CUSTOMER)
    ], primary_key=True)
