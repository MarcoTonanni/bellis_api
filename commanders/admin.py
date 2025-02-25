from django.contrib import admin
from commanders.models import Commander


@admin.register(Commander)
class CommanderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'death', 'procedence')
