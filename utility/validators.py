from django.core.exceptions import ValidationError

from E_Bank import settings


def bytes_to_megabytes(bytes):
    return bytes / 1000000


def validate_file_size(value):
    filesize = value.size

    if filesize > settings.FILE_SIZE_LIMIT:
        raise ValidationError(f"حداکثر سایز فایل می‌تواند {bytes_to_megabytes(settings.FILE_SIZE_LIMIT)}MB باشد")
    else:
        return value


def validate_phone_number(phone_number):
    if phone_number.startswith('09') and len(phone_number) == 11:
        # phone_number = '+98' + phone_number[1:]
        pass
    elif not phone_number.startswith('+98'):
        raise ValidationError(f"phone_number is not valid")
