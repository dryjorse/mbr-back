# Generated by Django 5.2.1 on 2025-06-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_remove_payment_user_payment_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('transfer', 'transfer'), ('tulpar', 'tulpar'), ('o-dengi', 'o-dengi')], max_length=255, verbose_name='Тип'),
        ),
    ]
