from django.core.exceptions import ValidationError


def validate_phone_number(phone_number):
    if phone_number.startswith('09') and len(phone_number) == 11:
        phone_number = '+98' + phone_number[1:]
    elif not phone_number.startswith('+98'):
        return False

    return True
