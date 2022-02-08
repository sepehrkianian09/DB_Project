from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from financial.models.loanProfit.types.loanProfitType import LoanProfitType


class LoanType(LoanProfitType):
    # loan_type_id = models.AutoField(primary_key=True)

    amount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(3000000000)
        ]
    )

    penalty_rate = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )