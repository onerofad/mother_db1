from rest_framework import serializers
from .models import Register, MakeRequest, Support, RegisterWatcher, Chats, Cards, Payment, Payments

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class MakeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MakeRequest

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Support

class RegisterWatcherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RegisterWatcher

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Chats

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cards

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Payments

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Payment
