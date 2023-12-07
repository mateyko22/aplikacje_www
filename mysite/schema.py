import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from polls.models import Osoba, Stanowisko


class OsobaType(DjangoObjectType):
    class Meta:
        model = Osoba
        fields = ("id", "imie", "nazwisko", "plec", "stanowisko")


class StanowiskoType(DjangoObjectType):
    class Meta:
        model = Stanowisko
        fields = ("id", "nazwa", "opis")


class Query(graphene.ObjectType):
    all_stanowiska = graphene.List(StanowiskoType)
    osoba_by_id = graphene.Field(OsobaType, id=graphene.Int(required=True))
    all_osobas = graphene.List(OsobaType)
    osoba_by_name = graphene.Field(OsobaType, name=graphene.String(required=True))
    find_osobas_name_by_phrase = graphene.List(OsobaType, substr=graphene.String(required=True))
    osoba_by_plec = graphene.List(OsobaType, plec=graphene.Int(required=True))
    osoba_by_data_dodania = graphene.List(OsobaType, data_dodania=graphene.Date(required=True))
    find_osoba_nazwisko_startswith = graphene.List(OsobaType, substr=graphene.String(required=True))

    def resolve_all_stanowiska(root, info):
        return Stanowisko.objects.all()

    def resolve_osoba_by_id(root, info, id):
        try:
            return Osoba.objects.get(pk=id)
        except Osoba.DoesNotExist:
            raise Exception('Invalid person Id')

    def resolve_osoba_by_name(root, info, name):
        try:
            return Osoba.objects.get(name=name)
        except Osoba.DoesNotExist:
            raise Exception(f'No Person with name \'{name}\' found.')

    def resolve_all_osobas(root, info):
        """ zwraca również wszystkie powiązane obiekty team dla tego obiektu Person"""
        return Osoba.objects.all()

    def resolve_find_osobas_name_by_phrase(self, info, substr):
        return Osoba.objects.filter(nazwisko__icontains=substr)

    def resolve_osoba_by_plec(self, info, plec):
        return Osoba.objects.filter(plec=plec)

    def resolve_osoba_by_data_dodania(self, info, data_dodania):
        return Osoba.objects.filter(data_dodania__gte=data_dodania)

    def resolve_find_osoba_nazwisko_startswith(self, info, substr):
        return Osoba.objects.filter(nazwisko__istartswith=substr)


schema = graphene.Schema(query=Query)
