# Generated by Django 3.2.16 on 2022-12-20 13:12

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20221220_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Rejected, try booking on a different hour', 'Rejected, try booking on a different hour')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_persons',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="'eg.+44'", max_length=128, null=True, region=None),
        ),
    ]