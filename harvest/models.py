from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


UNITS = [
    ('Basket', 'Basket'),
    ('Sack', 'Sack'),
    ('Kilogram', 'Kilogram'),
    ('Ton', 'Ton'),
    ('Barn', 'Barn')
]

SEASONS = [
    (1, 'Main Season'),
    (2, 'Lean Season')
]

class Harvest(models.Model):
    date = models.DateField(blank=True, null=True)
    crop = models.ForeignKey('crop.Crop', on_delete=models.SET_NULL, blank=True, null=True, related_name='harvest_crop')
    quantity = models.IntegerField(null=True, blank=True, default=0)
    unit = models.CharField(max_length=10, blank=True, null=True, choices=UNITS)
    season = models.IntegerField(null=True, blank=True, choices=SEASONS)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="harvests")

    class Meta:
        db_table = 'harvest'
        ordering = ['date']