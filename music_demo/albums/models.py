from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    tracks = models.IntegerField()
    length = models.CharField(max_length=6)

    def __str__(self):
        return self.name
