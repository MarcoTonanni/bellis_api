from django.contrib import admin
from wars.models import War


@admin.register(War)
class WarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'start_date',
        'end_date',
        'victor'
    )
