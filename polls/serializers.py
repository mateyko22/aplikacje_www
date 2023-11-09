from rest_framework import serializers
from .models import Osoba, Stanowisko
from datetime import date


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
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']
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
