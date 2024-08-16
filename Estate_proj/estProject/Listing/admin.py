

from django.contrib import admin
from .models import Listing, ListingImage, ListingVideo

admin.site.register(Listing)
admin.site.register(ListingImage)
admin.site.register(ListingVideo)

