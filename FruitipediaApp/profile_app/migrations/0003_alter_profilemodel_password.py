# Generated by Django 4.2.3 on 2024-05-09 18:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_alter_profilemodel_age_alter_profilemodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='password',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(20)], verbose_name='Password (Min 8 chars)'),
        ),
    ]
