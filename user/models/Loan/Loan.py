class Loan(models.Model):
    loan_id = models.BigAutoField(primary_key=True)

    start_date = models.DateField(
        validators=[
            #     date<now
            # >account_creation_Date
        ]
    )

