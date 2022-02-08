from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from .payment import Payment
from ..objects import Loan
from ... import CardToCardTransaction


# a class which turns to either payment or penalty(if transaction has crossed the line)
class PaymentPenalty(Payment):
    loan_profit_class = Loan
    loan_profit_id = models.ForeignKey(Loan, on_delete=models.CASCADE)

    # Transaction should be done in a right time and also right price
    def clean(self):
        super().clean()
        if self.card_to_card_transaction_id:
            c2c_transaction = CardToCardTransaction.objects.get(pk=self.card_to_card_transaction_id)

            selected_loan_profit = self.loan_profit_class.objects.get(pk=self.loan_profit_id)
            if c2c_transaction.dst != selected_loan_profit.bank_acc_id:
                raise ValidationError("Transaction is not valid. src != bank_acc_id")
            if c2c_transaction.src != selected_loan_profit.regular_acc_id:
                raise ValidationError("Transaction is not valid. dst != regular_acc_id")

            selected_type = self.loan_profit_class.type_class.objects.get(pk=selected_loan_profit.type_id)
            num_of_payments = selected_type.duration / selected_type.payment_duration

            payment_start_day = self.payment_index * selected_type.payment_duration * 30
            payment_end_day = payment_start_day + selected_type.payment_duration * 30

            transaction_day = (c2c_transaction.date - selected_loan_profit.start_date).days
            profit_price = selected_type.amount * (1 + selected_type.profit_rate) / num_of_payments
            payment_price = profit_price * (1 + selected_type.penalty_rate)
            if payment_start_day <= transaction_day <= payment_end_day:
                # if it's in interval, it should be
                if abs(profit_price - c2c_transaction.amount) > 0.1:
                    raise ValidationError("transaction value for payment is not valid")
            elif transaction_day > payment_end_day:
                if abs(payment_price - c2c_transaction.amount) > 0.1:
                    raise ValidationError("transaction value for penalty is not valid")
            else:
                raise ValidationError("transaction is not done in an appropriate time")

    # computables: type, cost_price, state
