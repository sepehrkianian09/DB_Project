from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from financial.models import CardToCardTransaction


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    loan_profit_class = None
    loan_profit_id = None
    card_to_card_transaction_id = models.ForeignKey(CardToCardTransaction, on_delete=models.CASCADE, null=True,
                                                    blank=True)
    payment_index = models.IntegerField(validators=[
        MinValueValidator(0)
    ])

    def clean(self):
        super().clean()
        selected_loan_profit = self.loan_profit_id
        selected_type = selected_loan_profit.type_id
        num_of_payments = selected_type.duration / selected_type.payment_duration
        if self.payment_index >= num_of_payments:
            raise ValidationError(f"payment index is bigger than loan_type_limit")

    class Meta:
        abstract = True
        unique_together = ['loan_profit_id', 'payment_index']
