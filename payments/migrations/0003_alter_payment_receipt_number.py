# Generated by Django 5.0.6 on 2024-09-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='receipt_number',
            field=models.CharField(editable=False),
        ),
    ]
