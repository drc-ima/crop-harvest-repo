from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Farm(models.Model):
    location = models.CharField(max_length=150, blank=True, null=True)
    size = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="farms")

    class Meta:
        db_table = 'farm'