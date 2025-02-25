from django.contrib import admin
from battles.models import Battle


@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'war',
        'victor'
    )
