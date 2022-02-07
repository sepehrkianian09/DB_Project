from django.core.validators import MaxValueValidator
from  django.db import models
from financial.transaction import DepositWithDrawTransaction
from  user.models.Employee import Employee
from  account.models.account import CustomerAccount
class DepoWidthTransactionLicense(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    depo_width_transaction_id = models.ForeignKey(DepositWithDrawTransaction, on_delete=models.CASCADE())
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE())

    customer_acc_id = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE())


    CARD_TO_CARD = 'C'
    DEPO_WIDTH_DRAW = 'D'
    TRANS_TYPE_CHOICES = ((CARD_TO_CARD, 'card_to_card'), (DEPO_WIDTH_DRAW, 'depo_width_draw'))
    type = models.CharField(
        max_length=1,
        choices=TRANS_TYPE_CHOICES,
        default=DEPO_WIDTH_DRAW
    )

    transaction_limit = models.IntegerField(

        validators=[
           MaxValueValidator ( 3000000)

    ]

    )

    expiration_date = models.DateField(
        validators=[
            #     date<now
            # >account_creation_Date
        ]
    )

