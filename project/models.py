from django.db import models

# Create your models here.
from django.db import models


        
class TimeStampModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class Brand(TimeStampModel):
    brand_name = models.CharField(max_length=200)
    brand_logo = models.ImageField(upload_to='image/')
    year = models.IntegerField()
    founder = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.brand_name)



  
        
class product(TimeStampModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    title = models.TextField(max_length=200)
    price = models.IntegerField()
    availability = models.BooleanField(default=False)
    color = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.id, self.brand)
        