from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProfitingType(models.Model):
    prof_type_id = models.AutoField(primarykey=True)

    profit_rate = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
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

    monthly_withdraw_limit = models.IntegerField(
        validators=[
            MaxValueValidator(50)
        ]
    )

    def clean(self):
        super().clean()
        if int(self.duration) % int(self.payment_duration) != 0:
            raise ValidationError(f"duration must be dividable by payment_duration")
