from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from FruitipediaApp.validators import validator_profile


class ProfileModel(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 25

    MIN_LEN_LAST_NAME = 1
    MAX_LEN_LAST_NAME = 35

    MAX_LEN_EMAIL = 40

    MIN_LEN_PASSWORD = 8
    MAX_LEN_PASSWORD = 20

    first_name = models.CharField(
        verbose_name='First Name',
        validators=[
            validator_profile.alpha_validator,
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            MaxLengthValidator(MAX_LEN_FIRST_NAME),
        ],
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        validators=[
            validator_profile.alpha_validator,
            MinLengthValidator(MIN_LEN_LAST_NAME),
            MaxLengthValidator(MAX_LEN_LAST_NAME),
        ],
    )

    email = models.EmailField(
        verbose_name='Email',
        validators=[
            MaxLengthValidator(MAX_LEN_EMAIL),
        ],
    )

    password = models.CharField(
        verbose_name='Password',
        validators=[
            MinLengthValidator(MIN_LEN_PASSWORD),
            MaxLengthValidator(MAX_LEN_PASSWORD),
        ],
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
    )

    age = models.IntegerField(
        verbose_name='Age',
        default='18',
        null=True,
    )
