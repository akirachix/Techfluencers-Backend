from django.db import models

# Create your models here.

class Clothes (models.Model):
   cloth_name = models.CharField(primary_key=True)
   cloth_exporter =models.CharField(max_length=40)
   cloth_material = models.CharField(max_length=40)
   trending_date = models.DateField()
   cloth_image = models.ImageField(default=1)
   cloth_id = models.IntegerField()




   def __str__(self):
     return f"{self.cloth_name}"




 
