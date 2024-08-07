from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'), 
    path('home/', views.home_view, name='home'),
    path('add_house_listing/', views.add_house_listing, name='add_house_listing'),
    path('view_house_listings/', views.view_house_listing, name='view_house_listings'),
    path('update_house_listing/<int:property_id>/', views.update_house_listing, name='update_house_listing'),
    path('delete_house_listing/<int:property_id>/', views.delete_house_listing, name='delete_house_listing'),
    
]
