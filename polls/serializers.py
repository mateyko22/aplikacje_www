from rest_framework import serializers
from .models import Osoba, Stanowisko


class StanowiskoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    nazwa = serializers.CharField(required=True)

    opis = serializers.CharField(required=True)


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']
        read_only_fields = ['data_dodania']
