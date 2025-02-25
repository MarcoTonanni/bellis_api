from django.contrib import admin
from factions.models import Faction


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
