from django.core.validators import MinValueValidator
from django.db import models

from financial.models.transaction import CardToCardTransaction
from account.models.account import ProfittingAccount


class ProfitPayment(models.Model):
    payment_penalty_id = models.BigAutoField(primary_key=True)
    profiting_account_id = models.ForeignKey(ProfittingAccount, on_delete=models.CASCADE)
    card_to_card_transaction_id = models.ForeignKey(CardToCardTransaction, on_delete=models.CASCADE, null=True,
                                                    blank=True)
    payment_index = models.IntegerField(validators=[
        MinValueValidator(0)
    ])

    def clean(self):
        super().clean()
        # selected_loan = ProfittingAccount.objects.get(pk=self.profiting_account_id)
        # selected_loan_type = ProfittingType.objects.get(pk=selected_loan)
        # if self.payment_index >= (selected_loan_type.duration / selected_loan_type.payment_duration):
        #     raise ValidationError(f"payment index is bigger than loan_type_limit")

    # computables: cost_price, state
    class Meta:
        unique_together = ['profiting_account_id', 'payment_index']
