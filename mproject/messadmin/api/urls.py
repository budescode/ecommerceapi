from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'messadmin_api'


urlpatterns = [
path('myproductslist/', views.MyProducts.as_view(), name='productlist'),
path('myproductsdetails/', views.MyProductDetails.as_view(), name='myproductsdetails'),
path('deletemyproduct/', views.DeleteMyProduct.as_view(), name='deletemyproduct'),
path('productcreate/', views.ProductsCreate.as_view(), name='productcreate'),

]