from django.db import models
from datetime import date
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


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
    data_dodania = models.DateField(default=date.today())
    wlasciciel = models.ForeignKey('auth.User', related_name='osoby', on_delete=models.CASCADE, null=True, blank=True)
    highlighted = models.TextField()

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ['nazwisko']
        verbose_name_plural = 'Osoby'

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                               full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super().save(*args, **kwargs)
