from django.db import models

# Create your models here.
class Payment(models.Model):
    
    services = models.CharField(max_length=30,blank=False)
    price = models.IntegerField(blank=False)
    cardholder = models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.cardholder