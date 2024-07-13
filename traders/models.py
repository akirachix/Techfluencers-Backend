from django.db import models
from clothes.models import Clothes

# Create your models here.
class Trader  (models.Model) :
    traders_id = models.IntegerField()
    traders_fullname = models.ForeignKey(Clothes,default=1, on_delete=models.CASCADE, related_name='traders')
    traders_email = models.EmailField()
    traders_location = models.TextField()
    traders_password = models.PositiveBigIntegerField()
    
      
         
         
    def __str__(self):
        return  f"{self.traders_id}"
    
