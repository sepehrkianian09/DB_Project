from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from datetime import date

from utility.validators import validate_file_size


def user_picture_path(instance, filename):
    return f'human/{instance.nationality_code}/{filename}'
    # return 'expense/{0}/{1}'.format(instance.payer.id, filename)


#     bigger equal than 18y
def validate_birthday_date(birthday_date):
    if (date.today() - birthday_date).days < 6574.365:
        raise ValidationError(f"you must be at least 18 years old")


class Human(models.Model):
    nationality_code = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10)])

    CUSTOMER = 'C'
    EMPLOYEE = 'E'
    TYPE_CHOICES = ((EMPLOYEE, 'employee'), (CUSTOMER, 'Customer'))
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=CUSTOMER,
        validators=[MinLengthValidator(1)]
    )

    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = ((MALE, 'male'), (FEMALE, 'female'))
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE,
        validators=[MinLengthValidator(1)]
    )

    picture = models.FileField(
        upload_to=user_picture_path,
        validators=[validate_file_size],
        null=True,
        blank=True
    )

    birthday_date = models.DateField(
        validators=[
            validate_birthday_date
        ]
    )
