from django.db import models
from account.models.loan import Loan
from account.models.transaction import CardToCardTransaction

class Payment_Penalty(models.Model):
    payement_Uniqueid = models.BigAutoField(primary_key=True)
    loan_acc_id = models.ForeignKey(Loan, on_delete=models.CASCADE())
    card_to_card_transaction = models.ForeignKey(CardToCardTransaction, on_delete=models.CASCADE())
    FEE = 'F'
    PAYMENT = 'P'
    PAYMENT_TYPE_CHOICES = ((FEE, 'fee'), (PAYMENT, 'payment'))
    type = models.CharField(
        max_length=1,
        choices=PAYMENT_TYPE_CHOICES,
        default=PAYMENT
    )

