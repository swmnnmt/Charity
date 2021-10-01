from rest_framework import serializers

from charities.models import Benefactor, Charity, Task


class BenefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefactor
        fields = ('experience', 'free_time_per_week',)

    def create(self, validated_data):
        user = self.context['request'].user
        benefactor = Benefactor.objects.create(user=user, **validated_data)
        return benefactor


class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ('name', 'reg_number',)

    def create(self, validated_data):
        user = self.context['request'].user
        charity = Charity.objects.create(user=user, **validated_data)
        return charity


class TaskSerializer(serializers.ModelSerializer):
    pass
