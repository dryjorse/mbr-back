# Generated by Django 5.0.6 on 2024-09-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payment_receipt_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_success',
            field=models.BooleanField(default=True, verbose_name='Проведен ли платеж'),
        ),
    ]
