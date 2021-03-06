# Generated by Django 3.1.4 on 2022-02-08 04:58

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import user.models.customer
import user.models.employee
import user.models.human
import utility.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('nationality_code', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)])),
                ('type', models.CharField(choices=[('E', 'employee'), ('C', 'Customer')], default='C', max_length=1, validators=[django.core.validators.MinLengthValidator(1)])),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=1, validators=[django.core.validators.MinLengthValidator(1)])),
                ('picture', models.FileField(blank=True, null=True, upload_to=user.models.human.user_picture_path, validators=[utility.validators.validate_file_size])),
                ('birthday_date', models.DateField(validators=[user.models.human.validate_birthday_date])),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.human', validators=[user.models.customer.validate_id])),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.human', validators=[user.models.employee.validate_id])),
                ('status', models.CharField(choices=[('O', 'employee'), ('F', 'Customer')], default='O', max_length=1)),
                ('monthly_salary', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('can_block_account', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HumanAddress',
            fields=[
                ('nationality_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.human')),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('zone', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('complete_address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='HumanName',
            fields=[
                ('nationality_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.human')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('fathers_name', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HumanPhoneNumber',
            fields=[
                ('phone_number', models.CharField(max_length=20, primary_key=True, serialize=False, validators=[utility.validators.validate_phone_number])),
                ('nationality_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.human')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeWorkingHours',
            fields=[
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.employee')),
                ('working_day', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)])),
                ('start_hour', models.TimeField(default=datetime.time(0, 0))),
                ('end_hour', models.TimeField(default=datetime.time(0, 0))),
            ],
            options={
                'unique_together': {('employee_id', 'working_day')},
            },
        ),
    ]
