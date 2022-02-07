from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
class Account(models.Model):
    acc_id=models.AutoField(primary_key=True)
    CUSTOMER = 'C'
    MANAGER = 'M'
    ACC_TYPE_CHOICES = ((MANAGER, 'Employee'), (CUSTOMER, 'Customer'))
    type = models.CharField(
        max_length=1,
        choices=ACC_TYPE_CHOICES,
        default=CUSTOMER
    )

    CLOSED = 'C'
    UNCLOSED = 'U'
    STATE_CHOICES = ((CLOSED, 'closed'), (UNCLOSED, 'unclosed'))
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default=CLOSED
    )

    balance = models.IntegerField(

        validators=[
            MinValueValidator(0)

        ]

    )

    creation_date = models.DateField(
        validators=[
            #     date<now
        ]
    )

