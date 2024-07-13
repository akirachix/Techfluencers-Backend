from django.db import models
from clothes.models import Clothes

# Create your models here.
class Exporter  (models.Model) :
    exporter_id = models.IntegerField()
    exporter_location = models.TextField()
    exporter_name = models.CharField(max_length=20)
    exporter_cloth = models.ForeignKey(Clothes,default=1, on_delete=models.CASCADE, related_name='exporters')

    def __str__(self):
          return f"{self.exporter_id}"