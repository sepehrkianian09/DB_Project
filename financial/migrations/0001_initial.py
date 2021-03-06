# Generated by Django 3.1.4 on 2022-02-08 04:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import financial.models.loan_and_profit.objects.loan
import financial.models.loan_and_profit.objects.profitingAccount


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardToCardTransaction',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(auto_now_add=True)),
                ('dst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardtocardtransaction_dst', to='account.account')),
                ('src', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardtocardtransaction_src', to='account.account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepositWithDrawTransaction',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)])),
                ('payment_duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)])),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3000000000)])),
                ('penalty_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfitingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)])),
                ('payment_duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)])),
                ('monthly_withdraw_limit', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfitingAccount',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.customeraccount', validators=[financial.models.loan_and_profit.objects.profitingAccount.validate_id])),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('bank_acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.bankaccount')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.profitingtype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(validators=[financial.models.loan_and_profit.objects.loan.check_if_is_future])),
                ('bank_acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.bankaccount')),
                ('regular_acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.regularaccount')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.loantype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepoWithTransactionLicense',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('D', 'deposit'), ('W', 'withdraw')], default='D', max_length=1)),
                ('transaction_limit', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3000000)])),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('customer_acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customeraccount')),
                ('depo_with_transaction_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.depositwithdrawtransaction', unique=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.employee')),
            ],
        ),
        migrations.CreateModel(
            name='ProfitPayment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_index', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('card_to_card_transaction_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.cardtocardtransaction')),
                ('loan_profit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.profitingaccount')),
            ],
            options={
                'abstract': False,
                'unique_together': {('loan_profit_id', 'payment_index')},
            },
        ),
        migrations.CreateModel(
            name='PaymentPenalty',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_index', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('card_to_card_transaction_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.cardtocardtransaction')),
                ('loan_profit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.loan')),
            ],
            options={
                'abstract': False,
                'unique_together': {('loan_profit_id', 'payment_index')},
            },
        ),
    ]
