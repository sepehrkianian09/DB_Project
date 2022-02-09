from django.core.exceptions import ValidationError
from django.db import models

from ..objects.profitingAccount import ProfitingAccount
from .payment import Payment
from ... import CardToCardTransaction


class ProfitPayment(Payment):
    loan_profit_class = ProfitingAccount
    loan_profit_id = models.ForeignKey(ProfitingAccount, on_delete=models.CASCADE)

    # transaction should be done in a right time. pricing is dynamic
    def clean(self):
        super().clean()
        if self.card_to_card_transaction_id:
            c2c_transaction = CardToCardTransaction.objects.get(pk=self.card_to_card_transaction_id)

            selected_loan_profit = self.loan_profit_class.objects.get(pk=self.loan_profit_id)
            if c2c_transaction.src != selected_loan_profit.bank_acc_id:
                raise ValidationError("Transaction is not valid. dst != bank_acc_id")
            if c2c_transaction.dst != selected_loan_profit.id:
                raise ValidationError("Transaction is not valid. src != profit_acc_id")

            selected_type = self.loan_profit_class.type_class.objects.get(pk=selected_loan_profit.type_id)
            num_of_payments = selected_type.duration / selected_type.payment_duration

            payment_start_day = self.payment_index * selected_type.payment_duration * 30
            payment_end_day = payment_start_day + selected_type.payment_duration * 30
            if not (payment_start_day <= (
                    c2c_transaction.date - selected_loan_profit.start_date).days <= payment_end_day):
                raise ValidationError("transaction is not done in an appropriate time")

    # computables: cost_price, state
