from django.contrib import admin
from citations.models import Citation


@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'war',
        'reliability',
        'text',
        'book',
    )
