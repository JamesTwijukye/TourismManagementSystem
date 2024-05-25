from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,blank=False)
    email = models.CharField(max_length=30,blank=False)
    phoneNumber = models.CharField(max_length=30,blank=False)
    subject = models.CharField(max_length=30,blank=False)
    message = models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.name + "@" +self.email+"with"+self.phoneNumber+"with aim of"+self.subject+"with a message of"+self.message