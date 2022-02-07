from django.db import models
from financial.models.transaction import Transaction
from account.models.account import Account


class CardToCardTransaction(models.Model):
    card_to_card_transaction_id = models.ForeignKey(Transaction, primarykey=True, on_delete=models.CASCADE())
    src = models.ForeignKey(Account, on_delete=models.CASCADE())
    dst = models.ForeignKey(Account, on_delete=models.CASCADE())
