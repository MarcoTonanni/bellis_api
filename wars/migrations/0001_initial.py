# Generated by Django 5.1.6 on 2025-02-19 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commanders', '0001_initial'),
        ('factions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='War',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('belligerents', models.ManyToManyField(related_name='wars_belligerents', to='factions.faction')),
                ('commanders', models.ManyToManyField(related_name='wars', to='commanders.commander')),
                ('victor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wars_victor', to='factions.faction')),
            ],
        ),
    ]
