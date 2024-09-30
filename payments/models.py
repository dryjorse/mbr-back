from django.db import models
from users.models import User
from django.utils import timezone
import random

class Payment(models.Model):
  TYPE_CHOISES = {
    "transfer": "transfer", 
    "tulpar": "tulpar",
    "o-dengi": "o-dengi"
  }

  type = models.CharField("Тип", max_length=255, choices=TYPE_CHOISES)
  summ = models.DecimalField("Цена", max_digits=6, decimal_places=2)
  geolocation = models.CharField("Адрес", max_length=255)
  is_success = models.BooleanField("Проведен ли платеж", default=True)
  fullname = models.CharField("Имя и фамилия", max_length=255, blank=True, null=True)
  phone = models.IntegerField("Номер телефона", blank=True, null=True)
  transport_code = models.IntegerField("Код транспорта", blank=True, null=True)
  receipt_number = models.CharField(editable=False)
  created_at = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
  users = models.ManyToManyField(User, related_name='payments_made')

  class Meta:
    verbose_name = "Платежи"
    verbose_name_plural = "Платежи"

  def save(self, *args, **kwargs):
    if not self.pk:
      self.receipt_number = f'P0815{random.randint(1000000000, 9999999999)}'

    super().save(*args, **kwargs)

  def __str__(self):
    return f'Платеж в сумме {self.summ}'
