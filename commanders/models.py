from django.db import models


NATIONALITY_CHOICES = (
    ('ROM', 'Roman'),
    ('GRK', 'Greek'),
    ('CAR', 'Carthaginian'),
    ('ITA', 'Italian'),
    ('HIS', 'Iberian'),
    ('GAU', 'Gaul'),
    ('GER', 'Germanic'),
    ('BRI', 'Brittanic'),
    ('PON', 'Pontic'),
    ('ARM', 'Armenian'),
    ('PER', 'Persian'),
    ('EGP', 'Egyptian'),
    ('MAU', 'Mauretanian'),
    ('NUM', 'Numidian'),
    ('PAR', 'Parthian'),
    ('MAK', 'Macedonian'),
    ('UNK', 'Unknown'),
)


class Commander(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)
    procedence = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
