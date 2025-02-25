from django.db import models
from wars.models import War
from factions.models import Faction
from commanders.models import Commander


class Battle(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    war = models.ForeignKey(
        War,
        on_delete=models.PROTECT,
        related_name='battles'
    )
    belligerents = models.ManyToManyField(Faction, related_name='battles_belligerants')
    commanders = models.ManyToManyField(Commander, related_name='battles')
    victor = models.ForeignKey(
        Faction,
        on_delete=models.PROTECT,
        related_name='battles_victor'
    )

    def __str__(self):
        return self.name
