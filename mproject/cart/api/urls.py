from django.urls import path
from . import views


app_name = 'cart_api'


urlpatterns = [
path('cartlist/', views.CartList.as_view(), name='cartlist'),
path('cartdetails/', views.CartDetails.as_view(), name='cartdetails'),
path('cartcreate/', views.CartCreate.as_view(), name='cartcreate'),
path('cartdelete/', views.CartDelete.as_view(), name='cartdelete'),



]