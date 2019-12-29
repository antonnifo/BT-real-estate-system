from django.urls import path 

from . import views

urlpatterns = [
    # /listing
    path('',views.listings, name='listings'),
    path('<int:id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
