from django.db import models


# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nazwa


class Osoba(models.Model):
    class PlecChoices(models.IntegerChoices):
        KOBIETA = 0, 'Kobieta'
        MĘŻCZYZNA = 1, 'Mężczyzna'
        INNA = 2, 'Inna'

    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    plec = models.CharField(choices=PlecChoices.choices)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ['nazwisko']
        verbose_name_plural = 'Osoby'


