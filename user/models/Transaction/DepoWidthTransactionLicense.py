class DepoWidthTransactionLicense(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    CARD_TO_CARD = 'C'
    DEPO_WIDTH_DRAW = 'D'
    TRANS_TYPE_CHOICES = ((CARD_TO_CARD, 'card_to_card'), (DEPO_WIDTH_DRAW, 'depo_width_draw'))
    type = models.CharField(
        max_length=1,
        choices=TRANS_TYPE_CHOICES,
        default=CARD_TO_CARD
    )

    transaction_limit = models.(

        validators=[
                   > 0, < 3000000

    ]

    )

    expiration_date = models.DateField(
        validators=[
            #     date<now
            # >account_creation_Date
        ]
    )

