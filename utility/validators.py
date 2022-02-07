from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import ngettext_lazy


@deconstructible
class FixedLengthValidator(BaseValidator):
    message = ngettext_lazy(
        'Ensure this value has exactly %(limit_value)d character (it has %(show_value)d).',
        'Ensure this value has exactly %(limit_value)d characters (it has %(show_value)d).',
        'limit_value')
    code = 'fixed_length'

    def compare(self, a, b):
        return a == b

    def clean(self, x):
        return len(x)
