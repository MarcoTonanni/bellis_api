# Generated by Django 5.1.6 on 2025-02-19 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='war',
            old_name='endDate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='war',
            old_name='startDate',
            new_name='start_date',
        ),
    ]
