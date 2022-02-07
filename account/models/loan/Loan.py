from django.db import models


class Loan(models.Model):
    loan_id = models.BigAutoField(primary_key=True)

    start_date = models.DateTimeField(
        validators=[
            #     date<now
            # >account_creation_Date
        ]
    )
