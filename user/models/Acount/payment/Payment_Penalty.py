class Payment_Penalty(models.Model):
    payement_Uniqueid = models.BigAutoField(primary_key=True)
    FEE = 'F'
    PAYMENT = 'P'
    PAYMENT_TYPE_CHOICES = ((FEE, 'fee'), (PAYMENT, 'payment'))
    type = models.CharField(
        max_length=1,
        choices=PAYMENT_TYPE_CHOICES,
        default=PAYMENT
    )


