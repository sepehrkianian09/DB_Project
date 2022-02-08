from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class LoanProfitType(models.Model):
    profit_rate = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
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

    def clean(self):
        super().clean()
        if int(self.duration) % int(self.payment_duration) != 0:
            raise ValidationError(f"duration must be dividable by payment_duration")

    class Meta:
        abstract = True
