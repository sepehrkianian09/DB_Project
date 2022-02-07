from django.db import models
from account.models.customerAccount import customerAccount


class TypeConversionTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    customer_acc_id = models.ForeignKey(customerAccount, on_delete=models.CASCADE)
    conversion_date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ['customer_acc_id', 'conversion_date']
