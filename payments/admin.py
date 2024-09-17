from django.contrib import admin
from .models import Payment
from django.utils.html import format_html
from django.utils.timezone import localtime

@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
  list_display = ('summ', 'get_users', 'fullname', 'geolocation', 'formatted_created_at')
  ordering = ['-created_at']
  readonly_fields = ['receipt_number']

  def get_users(self, obj):
    return ", ".join([user.username for user in obj.users.all()])  # users - это related_name из Payment
  get_users.short_description = 'Users'

  def formatted_created_at(self, obj):
    formatted_date = localtime(obj.created_at).strftime('%d.%m.%Y %H:%M:%S')
    return format_html(f'<span>{formatted_date}</span>')

  formatted_created_at.short_description = 'Дата создания'

