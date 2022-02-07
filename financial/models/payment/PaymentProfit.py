from django.db import models
from financial.models.transaction import CardToCardTransaction
from account.models.account import ProfittingAccount


class PaymentProfit(models.Model):
    payment_UniqueId = models.AutoField( primarykey=True)
    card_to_card_transaction = models.ForeignKey(CardToCardTransaction, on_delete=models.CASCADE())
    prof_acc_id = models.ForeignKey(ProfittingAccount, on_delete=models.CASCADE())
