from django.db import models

# Create your models here.

class GFG(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.hotel_name
    