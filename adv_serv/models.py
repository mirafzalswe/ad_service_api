from django.db import models

# Create your models here.
from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=255)
    ad_id = models.IntegerField(unique=True)
    author = models.CharField(max_length=255)
    views = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title