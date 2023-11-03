from polls.models import Osoba, Stanowisko
from polls.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# 1. stworzenie nowej instancji klasy Osoba
osoba = Osoba(imie='Jakub', nazwisko='Kowalski', plec=2, stanowisko=Stanowisko.objects.get(id=1))
osoba.save()

# 2. inicjalizacja serializera
serializer = OsobaSerializer(osoba)
serializer.data
# output:
# {'id': 4, 'imie': 'Jakub', 'nazwisko': 'Kowalski', 'plec': 2, 'stanowisko': 1, 'data_dodania': '2023-11-03'}

# 3. serializacja danych do formatu JSON
content = JSONRenderer().render(serializer.data)
content

# output
# b'{"id":4,"imie":"Jakub","nazwisko":"Kowalski","plec":2,"stanowisko":1,"data_dodania":"2023-11-03"}'


import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# tworzymy obiekt dedykowanego serializera i przekazujemy sparsowane dane
deserializer = OsobaSerializer(data=data)
deserializer.is_valid()
# output
# True


# aby upewnić się w jaki sposób wyglądają pola wczytanego serializera/deserializera, możemy wywołać zmienną deserializer.fields, aby wyświetlić te dane
deserializer.fields
# output
# {'id': IntegerField(label='ID', read_only=True), 'imie': CharField(max_length=60), 'nazwisko': CharField(max_length=60), 'plec': ChoiceField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inna')], validators=[<django.core.valid
# ators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>]), 'stanowisko': PrimaryKeyRelatedField(queryset=Stanowisko.objects.all()), 'data_dodania': DateField(read_only=True)}


# walidacja
deserializer.validated_data
# output
# OrderedDict([('imie', 'Jakub'), ('nazwisko', 'Kowalski'), ('plec', 2), ('stanowisko', <Stanowisko: Programista>)])

deserializer.save()
deserializer.data

# output
# {'id': 5, 'imie': 'Jakub', 'nazwisko': 'Kowalski', 'plec': 2, 'stanowisko': 1, 'data_dodania': '2023-11-03'}



# 1. stworzenie nowej instancji klasy Stanowisko
stanowisko = Stanowisko(nazwa='tester', opis='tester aplikacji')
stanowisko.save()

# 2. inicjalizacja serializera
serializer = StanowiskoSerializer(stanowisko)
serializer.data
# output:
# {'id': 3, 'nazwa': 'tester', 'opis': 'tester aplikacji'}

# 3. serializacja danych do formatu JSON
content = JSONRenderer().render(serializer.data)
content

# output
# b'{"id":3,"nazwa":"tester","opis":"tester aplikacji"}'

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# tworzymy obiekt dedykowanego serializera i przekazujemy sparsowane dane
deserializer = StanowiskoSerializer(data=data)
deserializer.is_valid()
# output
# True


# aby upewnić się w jaki sposób wyglądają pola wczytanego serializera/deserializera, możemy wywołać zmienną deserializer.fields, aby wyświetlić te dane
deserializer.fields
# output
# {'id': IntegerField(read_only=True), 'nazwa': CharField(required=True), 'opis': CharField(required=True)}


# walidacja
deserializer.validated_data
# output
# OrderedDict([('nazwa', 'tester'), ('opis', 'tester aplikacji')])

deserializer.save()
deserializer.data

# output
# {'id': 3, 'nazwa': 'tester', 'opis': 'tester aplikacji'}'