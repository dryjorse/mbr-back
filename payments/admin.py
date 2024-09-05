from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
  list_display = ('summ', 'user', 'geolocation')
  readonly_fields = ['receipt_number']

