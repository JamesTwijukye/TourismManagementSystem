from django.db import models

# Create your models here.
class Trip(models.Model):
    trip_id= models.CharField(max_length=30,blank=False)
    trip_text = models.CharField(max_length=730,blank=False)
    trip_tittle= models.CharField(max_length=730,blank=False)
    trip_price= models.IntegerField(blank=False)
    trip_image = models.ImageField(upload_to= "trip_images")

    def __str__(self):
        return self.trip_tittle
    
class LinkedImage(models.Model):
    image_id = models.CharField(max_length=50,blank=False)
    photo = models.ImageField(upload_to="linked_images")

    def __str__(self):
    
        return self.image_id
    
