from django.db import models
from django.utils import timezone

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    all_points = models.TextField(blank=True)
    closest_points = models.TextField(blank=True)
    date_created = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return str(self.id)
