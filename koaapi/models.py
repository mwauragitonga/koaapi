from django.db import models

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    all_points = models.TextField(blank=True)
    closest_points = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
