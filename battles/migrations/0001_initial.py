# Generated by Django 5.1.6 on 2025-02-19 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commanders', '0001_initial'),
        ('factions', '0001_initial'),
        ('wars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('belligerants', models.ManyToManyField(related_name='battles_belligerants', to='factions.faction')),
                ('commanders', models.ManyToManyField(related_name='battles', to='commanders.commander')),
                ('victor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='battles_victor', to='factions.faction')),
                ('war', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='battles', to='wars.war')),
            ],
        ),
    ]
