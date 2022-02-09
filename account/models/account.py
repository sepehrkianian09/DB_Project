from django.core.validators import MinValueValidator
from django.db import models


class Account(models.Model):
    acc_id = models.AutoField(primary_key=True)

    CUSTOMER = 'C'
    MANAGER = 'M'
    ACC_TYPE_CHOICES = ((MANAGER, 'Manager'), (CUSTOMER, 'Customer'))
    type = models.CharField(
        max_length=1,
        choices=ACC_TYPE_CHOICES,
        default=CUSTOMER
    )

    CLOSED = 'C'
    OPEN = 'O'
    STATE_CHOICES = ((CLOSED, 'closed'), (OPEN, 'open'))
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default=OPEN
    )

    balance = models.IntegerField(default=0, validators=[
        MinValueValidator(0)
    ])

    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
