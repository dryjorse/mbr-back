from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from payments.serializers import PaymentSerializer
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

class CustomUserCreateSerializer(UserCreateSerializer):
  class Meta(UserCreateSerializer.Meta):
    model = get_user_model()
    fields = ('email', 'password')

class RegisterUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  username = serializers.CharField(
    required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

  class Meta:
    model = User
    fields = ['email', 'password', 'username', 'phone']
    extra_kwargs = {
      'password': {'write_only': True, 'min_length': 3},
      'phone': {'required': True}
    }
    
  def create(self, validated_data):
    user = self.Meta.model.objects.create(
      email=validated_data['email'],
      username=validated_data['username'],
      phone=validated_data['phone']
    )

    user.set_password(validated_data['password'])
    user.save()

    return user
    
class ProfileSerializer(serializers.ModelSerializer):
  payments = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'phone', 'account', 'balance', 'payments']

  def get_payments(self, obj):
    payments = obj.user_payments.all().order_by('-created_at')
    serializer = PaymentSerializer(payments, many=True)
    return serializer.data