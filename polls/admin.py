from django.contrib import admin

from .models import Osoba
from .models import Stanowisko


@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'data_dodania',
    )

    @admin.display(description='Stanowisko')
    def stanowiskoid(self, obj):  # noqa: D102
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'

    list_display = ['nazwisko', 'imie', 'plec', 'stanowiskoid', 'data_dodania']
    list_filter = ('stanowisko', 'data_dodania',)


@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ('nazwa',)
