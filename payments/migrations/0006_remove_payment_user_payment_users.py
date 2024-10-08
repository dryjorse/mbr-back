# Generated by Django 5.0.6 on 2024-09-17 16:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_payment_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='users',
            field=models.ManyToManyField(related_name='payments_made', to=settings.AUTH_USER_MODEL),
        ),
    ]
