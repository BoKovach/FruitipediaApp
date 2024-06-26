from django.core.exceptions import ValidationError


def alpha_validator(value):
    if not value[0].isalpha:
        raise ValidationError('"Your name must start with a letter!"')
