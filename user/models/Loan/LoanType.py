class Transaction(models.Model):
    loan_type_id = models.BigAutoField(primary_key=True)
    duration=models.(

    )
    amount = models.(

        validators=[
                   > 0, < 3000000

    ]

    )
    payback_amount = models.(

        validators=[
                   > 0, < 3000000

    ]

    )
    profit_rate(
        #<100
    )
    penalty_rate(

    )



