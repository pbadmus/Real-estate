from django.db import models

# Create your models here.

class Housing(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    MLS_no = models.CharField(max_length=15)
    exterior_acre = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    status = [
        ('Available'),
        ('Not Available'),
    ]
    description = models.TextField()
    
    def __str__(self): 
        return self.title
    
    
    
