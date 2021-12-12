from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

CROP_TYPES = [
    ('Cereal', 'Cereal'),
    ('Grain', 'Grain'),
    ('Tuber', 'Tuber'),
    ('Fruit', 'Fruit'),
    ('Cash', 'Cash Crop'),
    ('Vegetable', 'Vegetable'),
]

class Crop(models.Model):
    image = models.FileField(upload_to="crops/", blank=True, null=True)
    crop_type = models.CharField(max_length=150, blank=True, null=True, choices=CROP_TYPES)
    description = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name="crops", null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'crops'
        ordering = ['description', 'crop_type']

    # on delete types
    # set null
    # do nothing
    # cascade