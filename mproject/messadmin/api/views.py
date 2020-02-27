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
from messadmin.api.serializers import ProductsSerializer, ProductsCreateSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response


@method_decorator(csrf_exempt, name='dispatch')
class ProductsCreate(generics.CreateAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductsCreateSerializer
	permission_classes = [
	    permissions.IsAuthenticated, permissions.IsAdminUser
	]
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class MyProducts(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ProductsSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated, permissions.IsAdminUser
	]
	def get_queryset(self):
		qs = Products.objects.all().filter(user = self.request.user)
		print(qs)
		return qs

class DeleteMyProduct(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ProductsSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated, permissions.IsAdminUser
	]
	def get_queryset(self):
		id = self.request.GET.get('id')
		qs = Products.objects.filter(user = self.request.user)
		qs1 = qs.filter(id=id)
		qs1.delete()
		return qs

class MyProductDetails(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ProductsSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated, permissions.IsAdminUser
	]
	def get_queryset(self):
		id = self.request.GET.get('id')
		qs = Products.objects.filter(user = self.request.user, id=id)
		return qs
