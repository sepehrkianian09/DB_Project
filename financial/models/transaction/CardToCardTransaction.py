from django.db import models
from financial.models.transaction import Transaction
from account.models import account


class CardToCardTransaction(models.Model):
    card_to_card_transaction_id = models.ForeignKey(Transaction, primarykey=True, on_delete=models.CASCADE())
    src = models.ForeignKey(account, on_delete=models.CASCADE())
    dst = models.ForeignKey(account, on_delete=models.CASCADE())
