from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account.models.account import RegularAccount
from account.models.account import BankAccount

class LoanType(models.Model):
    loan_type_id = models.AutoField(primary_key=True)

    amount = models.IntegerField(

        validators=[
            MaxValueValidator(3000000000)

        ]

    )
   #payback amount sefate majazi nazashtam
    duration = models.IntegerField(

        validators=[
            MaxValueValidator(10)

        ]

    )
    payment_duration = models.IntegerField(


    )
    profit_rate = models.IntegerField(

        validators=[
            MaxValueValidator(50)

        ]

    )

    penalty_rate = models.IntegerField(

        validators=[
            MaxValueValidator(5)

        ]

    )
    addition_penalty_rate = models.IntegerField(

        validators=[
            MaxValueValidator(2)

        ])



