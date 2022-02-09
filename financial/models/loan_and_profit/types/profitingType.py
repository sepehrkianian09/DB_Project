from django.core.validators import MaxValueValidator
from django.db import models

from financial.models.loan_and_profit.types.loanProfitType import LoanProfitType


class ProfitingType(LoanProfitType):
    # prof_type_id = models.AutoField(primarykey=True)

    payment_withdraw_limit = models.IntegerField(
        validators=[
            MaxValueValidator(50)
        ]
    )
