from django.test import TestCase

from ..models import Osoba
from ..models import Stanowisko
from datetime import date


class OsobaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        stanowisko1 = Stanowisko.objects.create(nazwa='testowe_stanowisko nu', opis='do testow')
        stanowisko2 = Stanowisko.objects.create(nazwa='stanowisko_dwa', opis='do testow numer 2')
        Osoba.objects.create(imie='Jan', nazwisko='Piekarz', plec=2, stanowisko=stanowisko1)

    def test_first_name_label(self):
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('imie').max_length
        self.assertEqual(max_length, 60)

    def test_data_dodania(self):
        osoba = Osoba.objects.get(id=1)
        self.assertGreaterEqual(date.today(), osoba.data_dodania)

    def test_nazwisko_isalpha(self):
        osoba = Osoba.objects.get(id=1)
        self.assertTrue(osoba.nazwisko.isalpha())

    def test_stanowisko_ids(self):
        stanowisko_list = Stanowisko.objects.values_list('id', flat=True)
        self.assertListEqual(stanowisko_list, sorted(stanowisko_list))
