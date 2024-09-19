from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = ['id', 'type', 'summ', 'fullname', 'phone', 'transport_code', 'geolocation', 'receipt_number', 'is_success', 'created_at', 'users']
    read_only_fields = ['created_at', 'receipt_number']

  def validate_summ(self, value):
    if value <= 0:
      raise serializers.ValidationError("Summ must be greater than zero.")
    return value

  def create(self, validated_data):
    # Получаем пользователя из контекста
    user = self.context['request'].user
    users = validated_data.pop('users', None)  # Получаем других пользователей из данных

    # Проверяем баланс пользователя, если тип не "tulpar"
    summ = validated_data['summ']
    type = validated_data['type']

    if type != "tulpar":
      if user.balance < summ:
        raise serializers.ValidationError("Insufficient balance.")
      
      # Вычитаем сумму из баланса пользователя
      user.balance -= summ
      user.save()

    # Создаем объект Payment без поля users
    payment = Payment.objects.create(**validated_data)

    # Добавляем текущего пользователя в поле users
    payment.users.add(user)

    # Если в запросе переданы другие пользователи, добавляем их
    if users:
      payment.users.add(*users)

    return payment
