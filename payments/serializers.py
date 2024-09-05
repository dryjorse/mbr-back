from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = ['id', 'type', 'summ', 'fullname', 'phone', 'transport_code', 'geolocation', 'receipt_number', 'is_success', 'created_at']
    read_only_fields = ['user', 'created_at', 'receipt_number']

  def validate_summ(self, value):
    if value <= 0:
      raise serializers.ValidationError("Summ must be greater than zero.")
    return value

  def create(self, validated_data):
    user = self.context['request'].user
    summ = validated_data['summ']

    if user.balance < summ:
      raise serializers.ValidationError("Insufficient balance.")

    user.balance -= summ
    user.save()

    payment = Payment.objects.create(user=user, **validated_data)
    return payment
