from django.core.exceptions import ValidationError
from django.db import models

from E_Bank import settings


def bytes_to_megabytes(bytes):
    return bytes / 1000000


def validate_file_size(value):
    filesize = value.size

    if filesize > settings.FILE_SIZE_LIMIT:
        raise ValidationError(f"حداکثر سایز فایل می‌تواند {bytes_to_megabytes(settings.FILE_SIZE_LIMIT)}MB باشد")
    else:
        return value


class Human(models.Model):
    nationality_code = models.CharField(primary_key=True, max_length=10, validators=[])

    CUSTOMER = 'C'
    EMPLOYEE = 'E'
    TYPE_CHOICES = ((EMPLOYEE, 'Employee'), (CUSTOMER, 'Customer'))
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=CUSTOMER
    )

    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = ((MALE, 'male'), (FEMALE, 'female'))
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE
    )

    @staticmethod
    def user_picture_path(instance, filename):
        return f'human/{instance.nationality_code}/{filename}'
        # return 'expense/{0}/{1}'.format(instance.payer.id, filename)

    picture = models.FileField(
        upload_to=user_picture_path,
        validators=[validate_file_size],
        null=True,
        blank=True
    )

    birthday_date = models.DateField(
        validators=[
            #     bigger equal than 18y
        ]
    )

    # todo دو جدول Customer و Employee کلید مشترک نداشته باشن، و وقتی داخل Human‌ یکی typeش هر چیزی هست، تو جدول مخالفش دگ اون id‌ موجود نباشه.
