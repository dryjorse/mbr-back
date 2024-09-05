from rest_framework.viewsets import ModelViewSet
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

class PaymentsView(ModelViewSet):
  queryset = Payment.objects.all()
  serializer_class = PaymentSerializer

class PaymentCreateView(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = PaymentSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      try:
        payment = serializer.save()
        return Response({
          'id': payment.id,
          'summ': payment.summ,
          'fullname': payment.fullname,
          'phone': payment.phone,
          'transport_code': payment.transport_code,
          'geolocation': payment.geolocation,
          'receipt_number': payment.receipt_number,
          'is_success': payment.is_success,
          'created_at': payment.created_at
        }, status=status.HTTP_201_CREATED)
      except serializers.ValidationError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)