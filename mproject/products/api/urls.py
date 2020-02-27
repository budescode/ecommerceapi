from django.urls import path
from . import views


app_name = 'products_api'


urlpatterns = [
path('productslist/', views.ProductsList.as_view(), name='productlist'),
path('productdetails/', views.ProductDetails.as_view(), name='productdetails'),


]