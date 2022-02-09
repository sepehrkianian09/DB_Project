from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CardToCardTransaction)
admin.site.register(DepositWithDrawTransaction)
admin.site.register(DepoWithTransactionLicense)
admin.site.register(LoanType)
admin.site.register(ProfitingType)
admin.site.register(Loan)
admin.site.register(ProfitingAccount)
admin.site.register(PaymentPenalty)
admin.site.register(ProfitPayment)
