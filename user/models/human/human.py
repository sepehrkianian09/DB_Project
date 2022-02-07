from django.core.exceptions import ValidationError
from django.db import models

from E_Bank import settings
from utility.validators import FixedLengthValidator
from datetime import date


def bytes_to_megabytes(bytes):
    return bytes / 1000000


def validate_file_size(value):
    filesize = value.size

    if filesize > settings.FILE_SIZE_LIMIT:
        raise ValidationError(f"حداکثر سایز فایل می‌تواند {bytes_to_megabytes(settings.FILE_SIZE_LIMIT)}MB باشد")
    else:
        return value


def user_picture_path(instance, filename):
    return f'human/{instance.nationality_code}/{filename}'
    # return 'expense/{0}/{1}'.format(instance.payer.id, filename)


def validate_birthday_date(birthday_date):
    return (date.today() - birthday_date).days > 6574.365


class Human(models.Model):
    nationality_code = models.CharField(max_length=10, primary_key=True, validators=[FixedLengthValidator(10)])

    CUSTOMER = 'C'
    EMPLOYEE = 'E'
    TYPE_CHOICES = ((EMPLOYEE, 'employee'), (CUSTOMER, 'Customer'))
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=CUSTOMER,
        validators=[FixedLengthValidator(1)]
    )

    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = ((MALE, 'male'), (FEMALE, 'female'))
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE,
        validators=[FixedLengthValidator(1)]
    )

    picture = models.FileField(
        upload_to=user_picture_path,
        validators=[validate_file_size],
        null=True,
        blank=True
    )

    birthday_date = models.DateField(
        validators=[
            #     bigger equal than 18y
            validate_birthday_date
        ]
    )
