from django.core.validators import
from  django.db import models
from user.models.Acount import CustomerAccount
#todo: chejuri type ghablish nabashe mahdudiyat bezarim
class TypeConversionTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    customer_acc_id=models.ForeignKey(CustomerAccount,on_delete=models.CASCADE())
    NORMAL = 'N'
    PROFITTING = 'P'
    CUSTOMER_ACC_TYPE_CHOICES = ((PROFITTING, 'profiting'), (NORMAL, 'normal'))
    type = models.CharField(
        max_length=1,
        choices=CUSTOMER_ACC_TYPE_CHOICES,
        default=NORMAL
    )
    conversion_date = models.DateField(
        validators=[
            #     date<now
            # >account_creation_Date
        ]
    )