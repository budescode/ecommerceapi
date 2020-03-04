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
from products.models import Products, Categories
from products.api.serializers import ProductListSerializer, CategoriesListSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes




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

class CategoriesList(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CategoriesListSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.AllowAny
	]
	def get_queryset(self):
		qs = Categories.objects.all()
		return qs

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def ProductsView(request):
    qs = Products.objects.all()
    category = Categories.objects.all()
    return Response({'products': ProductListSerializer(qs, many=True).data, 'category':CategoriesListSerializer(category, many=True).data}, status=status.HTTP_404_NOT_FOUND)
    #return Response(qs)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def ProductsDetail(request):
    id = request.GET.get('id')
    qs = Products.objects.filter(id=id)
    if qs:
        cate = qs[0].category
        category = Categories.objects.get(name=cate)
        related_products = Products.objects.filter(category=category).exclude(id=qs[0].id)
        return Response({'products': ProductListSerializer(qs, many=True).data[0], 'related_products': ProductListSerializer(related_products, many=True).data})
    else:
        return Response({'error':'details does not exist'})


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