from django.db import models # type: ignore

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30,blank=False)
    password = models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.email + "@" +self.password

