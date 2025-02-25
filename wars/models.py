from django.db import models
from factions.models import Faction
from commanders.models import Commander


class War(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    belligerents = models.ManyToManyField(Faction, related_name='wars_belligerents')
    victor = models.ForeignKey(
        Faction,
        related_name='wars_victor',
        on_delete=models.PROTECT,
    )
    commanders = models.ManyToManyField(Commander, related_name='wars')

    def __str__(self):
        return self.name
