from django.db import models
from django.contrib.auth.models import User

FUNISHED_STATE = {
    ('FF', 'Fully Furnished'),
    ('SF', 'Semi Furnished'),
    ('NF', 'Not Furnished'),
}

class Listing(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    price_per_month = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    negotiable = models.BooleanField(default=False)
    bedrooms = models.IntegerField(blank=True, null=True)
    square_size = models.IntegerField(blank=True, null=True)
    lot_size = models.FloatField(blank=True, null=True)
    garage = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    boys_quarters = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    furnished_state = models.CharField(max_length=20, choices=FUNISHED_STATE, blank=True)
    
    
    
    def __str__(self):
        return self.title

# To allow multiple image uploading 
class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='property_pictures/')
    
    def __str__(self):
        return f"image for {self.listing.title}"
    
class ListingVideo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='video')
    video = models.FileField(upload_to='property_videos/')
    
    def __str__(self):
        return f"video for {self.listing.title}"
    
    
    
