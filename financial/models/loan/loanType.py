from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account.models.account import RegularAccount
from account.models.account import BankAccount


class LoanType(models.Model):
    loan_type_id = models.AutoField(primary_key=True)

    amount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(3000000000)
        ]
    )

    # duration is in month
    duration = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(120)
        ]
    )
    payment_duration = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(120)
        ]
    )

    profit_rate = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    penalty_rate = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def clean(self):
        super().clean()
        if int(self.duration) % int(self.payment_duration) != 0:
            raise ValidationError(f"duration must be dividable by payment_duration")
