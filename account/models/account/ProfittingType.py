from django.core.validators import MaxValueValidator
from django.db import models
from user.models import Manager


from account.models.account import Account

class ProfittingType(models.Model):
    prof_type_id=models.AutoField(Account, primarykey=True)
    CLOSED = 'C'
    UNCLOSED = 'U'
    STATE_CHOICES = ((CLOSED, 'closed'), (UNCLOSED, 'unclosed'))
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default=CLOSED
    )

    rate = models.IntegerField(

        validators=[
            MaxValueValidator(100)

        ]

    )
    duration = models.IntegerField(

        validators=[
            MaxValueValidator(50)

        ]

    )
    monthly_withdraw_limit = models.IntegerField(

        validators=[
            MaxValueValidator(50)

        ]

    )
