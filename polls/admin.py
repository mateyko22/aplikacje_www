from django.contrib import admin

from .models import Person
from .models import Osoba
from .models import Stanowisko

admin.site.register(Person)
admin.site.register(Stanowisko)


@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'data_dodania',
    )

    list_display = ['nazwisko', 'imie', 'plec', 'stanowisko', 'data_dodania']