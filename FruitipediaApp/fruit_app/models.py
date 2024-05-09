from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from FruitipediaApp.validators import validator_fruit


class FruitModel(models.Model):
    name = models.CharField(
        verbose_name='Name',
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(30),
            validator_fruit.alpha_validator,
        ]
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    description = models.TextField(verbose_name='Description',)

    nutrition = models.TextField(
        verbose_name='Nutrition',
        null=True,
    )
