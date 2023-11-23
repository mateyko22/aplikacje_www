from rest_framework import serializers
from .models import Osoba, Stanowisko
from datetime import date
from django.contrib.auth.models import User


class StanowiskoSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    nazwa = serializers.CharField(required=True)

    opis = serializers.CharField(required=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance


class OsobaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania', 'owner']
        # read_only_fields = ['data_dodania']

    def validate_nazwisko(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Nazwisko powinno zawierać tylko litery!",
            )
        return value

    def validate_data_dodania(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Data nie może być z przyszłości!",
            )
        return value


class UserSerializer(serializers.ModelSerializer):
    osoby = serializers.PrimaryKeyRelatedField(many=True, queryset=Osoba.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'osoby']