from rest_framework import serializers

from core.models import Card, Poll, Comparison


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Card


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Poll


class ComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comparison
