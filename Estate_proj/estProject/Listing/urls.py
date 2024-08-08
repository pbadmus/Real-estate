from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_listing, name='create_listing'),
   # path('view_house_listings/', views.view_house_listing, name='view_house_listings'),
  #  path('update_house_listing/<int:property_id>/', views.update_house_listing, name='update_house_listing'),
   # path('delete_house_listing/<int:property_id>/', views.delete_house_listing, name='delete_house_listing'),
]
