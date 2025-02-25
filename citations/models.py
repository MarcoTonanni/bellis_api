from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from wars.models import War


class Citation(models.Model):
    author = models.CharField(max_length=80)
    war = models.ForeignKey(
        War,
        on_delete=models.PROTECT,
        related_name='citations'
    )

    # Just for practicing, using a 5-star avaliation
    # for how trustworthy is that citation
    reliability = models.IntegerField(
        validators=[
            MinValueValidator(0, 'The minimum reliability value is 0.'),
            MaxValueValidator(5, 'The maximum reliability value is 5.'),
        ]
    )

    text = models.TextField()
    book = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.author
