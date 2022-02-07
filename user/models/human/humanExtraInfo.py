from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from user.models.human import Human


class HumanPhoneNumber(models.Model):
    nationality_code = models.ForeignKey(Human, on_delete=models.CASCADE)
    phone_number = models.CharField(primary_key=True, validators=[], max_length=20)


class HumanName(models.Model):
    nationality_code = models.ForeignKey(Human, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20, blank=True)


class HumanAddress(models.Model):
    nationality_code = models.ForeignKey(Human, on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zone = models.IntegerField(validators=[
        MinValueValidator(0)
    ], null=True, blank=True)
    complete_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, validators=[
        MinLengthValidator(10)
    ])
