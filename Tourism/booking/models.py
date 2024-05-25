from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_id = models.IntegerField(blank=False)
    hotel_name = models.CharField(max_length=50,blank=False)
    hotel_photo = models.ImageField(upload_to="hotel_images")


    def __str__(self):
        return self.hotel_name

class Booking(models.Model):
    hotel_id = models.CharField(max_length=100, blank=False, default="")
    personal_name = models.CharField(max_length=100 ,default="")
    personal_mobile = models.CharField(max_length=100,default="")
    total = models.CharField(max_length=100, default="")
    personal_nin = models.CharField(max_length=100,default="")
    number_of_adults = models.CharField(max_length=100,  default="")
    number_of_children = models.CharField(max_length=100,  default="")
    number_of_rooms = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.personal_name

class FeaturedDestination(models.Model):
    dest_id= models.CharField(max_length=230,blank=False)
    dest_text = models.CharField(max_length=530,blank=False)
    dest_tittle= models.CharField(max_length=530,blank=False)
    dest_image = models.ImageField(upload_to= "dest_images")

    def __str__(self):
        return self.dest_tittle
    
class HomeImages(models.Model):
    hm_id= models.CharField(max_length=230,blank=False)
    hm_image = models.ImageField(upload_to= "hm_images")

    def __str__(self):
        return self.hm_id





        
    