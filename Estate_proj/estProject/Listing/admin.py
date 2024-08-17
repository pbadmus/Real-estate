

from django.contrib import admin
from .models import Listing, ListingImage, ListingVideo

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "price", "bedrooms")

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingImage)
admin.site.register(ListingVideo)

