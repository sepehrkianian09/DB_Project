from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from financial.models.loan import Loan, LoanType
from financial.models.transaction import cardToCardTransaction


class PaymentPenalty(models.Model):
    payment_penalty_id = models.BigAutoField(primary_key=True)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    card_to_card_transaction_id = models.ForeignKey(cardToCardTransaction, on_delete=models.CASCADE, null=True,
                                                    blank=True)
    payment_index = models.IntegerField(validators=[
        MinValueValidator(0)
    ])

    def clean(self):
        super().clean()
        selected_loan = Loan.objects.get(pk=self.loan_id)
        selected_loan_type = LoanType.objects.get(pk=selected_loan.loan_type_id)
        if self.payment_index >= (selected_loan_type.duration / selected_loan_type.payment_duration):
            raise ValidationError(f"payment index is bigger than loan_type_limit")

    # computables: type, cost_price, state
    class Meta:
        unique_together = ['loan_id', 'payment_index']


