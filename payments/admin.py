from django.contrib import admin
from .models import Payment
from django.utils.html import format_html
from django.utils.timezone import localtime

@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
  list_display = ('summ', 'user', 'geolocation', 'formatted_created_at')
  ordering = ['created_at']
  readonly_fields = ['receipt_number']

  def formatted_created_at(self, obj):
    formatted_date = localtime(obj.created_at).strftime('%d.%m.%Y %H:%M:%S')
    return format_html(f'<span>{formatted_date}</span>')

  formatted_created_at.short_description = 'Дата создания'

