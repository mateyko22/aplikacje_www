from django.db import models


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nazwa


class Osoba(models.Model):
    class PlecChoices(models.IntegerChoices):
        KOBIETA = 1
        MĘŻCZYZNA = 2
        INNA = 3

    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    plec = models.IntegerField(choices=PlecChoices.choices)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ['nazwisko']
        verbose_name_plural = 'Osoby'


