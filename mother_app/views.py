from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, MakeRequest, Support, RegisterWatcher, Chats, Cards, Payment, Payments
from .serializers import RegisterSerializer, MakeRequestSerializer, SupportSerializer, RegisterWatcherSerializer, ChatSerializer, CardSerializer, PaymentSerializer, PaymentsSerializer

# stripe things
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status

# Create your views here.
class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class MakeRequestView(viewsets.ModelViewSet):
    queryset = MakeRequest.objects.all()
    serializer_class = MakeRequestSerializer

class SupportView(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

class RegisterWatcherView(viewsets.ModelViewSet):
    queryset = RegisterWatcher.objects.all()
    serializer_class = RegisterWatcherSerializer

class ChatView(viewsets.ModelViewSet):
    queryset = Chats.objects.all()
    serializer_class = ChatSerializer

class CardView(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer

class PaymentsView(viewsets.ModelViewSet):
    queryset = Payments.objects.order_by('created_at').all()
    serializer_class = PaymentsSerializer

class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class CreatePaymentIntentView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        currency = request.data.get("currency")
        email = request.data.get("user_email")

        if not email:
            return Response({'error': 'Invalid email'}, status=400)
        if not amount or int(amount) <= 0:
            return Response({'error': 'Invalid amount'}, status=400)
        if not currency:
            return Response({'error': 'Currency is required'}, status=400)

        supported_currencies = ['usd', 'eur', 'huf']
        if currency.lower() not in supported_currencies:
            return Response({'error': 'Unsupported currency'}, status=400)

        try:
            intent = stripe.PaymentIntent.create(
                amount = int(amount),
                currency = currency,
            )
            # Save to the database
            payment_data = {
                'amount': amount,
                'currency': currency,
                'stripe_payment_id': intent['id'],
                'user_email': email
            }
            serializer = PaymentSerializer(data=payment_data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'clientSecret': intent['client_secret'],
                    'payment': serializer.data,
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.StripeSrror as e:
            return Response({'error': str(e)}, status=400)


