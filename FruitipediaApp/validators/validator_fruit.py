from django.core.exceptions import ValidationError


def alpha_validator(value):
    if not value.isalpha:
        raise ValidationError("Fruit name should contain only letters!")
