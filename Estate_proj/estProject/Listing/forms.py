from django import forms
from .models import Listing

from django import forms
from django.forms import modelformset_factory
from .models import Listing, ListingImage, ListingVideo

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'address', 'city', 'price', 'price_per_month',
                  'negotiable', 'bedrooms', 'square_size', 'lot_size', 'garage', 'swimming_pool', 
                  'boys_quarters', 'furnished']

# Formsets for images and videos
ListingImageFormSet = modelformset_factory(ListingImage, fields=['image'], extra=5)
ListingVideoFormSet = modelformset_factory(ListingVideo, fields=['video'], extra=5)
