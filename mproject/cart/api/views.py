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
from cart.models import Cart
from products.models import Products
from cart.api.serializers import CartSerializer, CartCreateSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response




class CartList(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CartSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated
	]
	def get_queryset(self):
		qs = Cart.objects.all().filter(user=self.request.user)
		return qs

class CartDetails(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CartSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated
	]
	def get_queryset(self):
	    id = self.request.GET.get('id')
	    qs = Cart.objects.all().filter(id=id, user=self.request.user)
	    return qs

class CartDelete(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CartSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated
	]
	def get_queryset(self):
	    id = self.request.GET.get('id')
	    qs = Cart.objects.all().filter(user=self.request.user)
	    qs1 = qs.filter(id=id)
	    qs1.delete()
	    return qs

@method_decorator(csrf_exempt, name='dispatch')
class CartCreate(generics.CreateAPIView):
	queryset = Cart.objects.all()
	serializer_class = CartCreateSerializer
	permission_classes = [
	    permissions.IsAuthenticated
	]
	def perform_create(self, serializer):
	    id = self.request.GET.get('id')
	    product = Products.objects.get(id=id)
	    qty = serializer.validated_data['qty']
	    amount = qty * product.amount
	    serializer.save(user=self.request.user, product=product, amount = amount)