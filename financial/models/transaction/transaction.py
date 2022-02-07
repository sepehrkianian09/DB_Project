from django.core.validators import MinValueValidator
from django.db import models


class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)

    CARD_TO_CARD = 'C'
    DEPO_WITH = 'D'
    TRANS_TYPE_CHOICES = ((CARD_TO_CARD, 'card_to_card'), (DEPO_WITH, 'depo_width_draw'))
    type = models.CharField(
        max_length=1,
        choices=TRANS_TYPE_CHOICES,
        default=CARD_TO_CARD
    )

    amount = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    date = models.DateField(auto_now_add=True, editable=False)
