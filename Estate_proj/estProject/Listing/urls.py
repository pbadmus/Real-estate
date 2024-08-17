from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_listing, name='create_listing'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path('success/', views.success_page, name='success_page'),
    path('view_listing/', views.view_listing, name='view_listing'),  #  path('update_house_listing/<int:property_id>/', views.update_house_listing, name='update_house_listing'),
   # path('delete_house_listing/<int:property_id>/', views.delete_house_listing, name='delete_house_listing'),
]
