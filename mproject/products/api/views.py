from rest_framework import generics
from rest_framework import permissions
from .pagination import PostLimitOffsetPagination
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
    )
from django.db.models import Q
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from products.models import Products
from products.api.serializers import ProductListSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response




class ProductsList(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ProductListSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.AllowAny
	]
	def get_queryset(self):
		qs = Products.objects.all()
		return qs


class ProductDetails(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ProductListSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.AllowAny
	]
	def get_queryset(self):
		id = self.request.GET.get('id')
		qs = Products.objects.filter(id=id)
		return qs