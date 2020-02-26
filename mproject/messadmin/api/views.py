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
from messadmin.api.serializers import ProductsSerializer, ProductsCreateSerializer, MessAdminSerializer
from messadmin.models import MessModel
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
		adminmess = MessModel.objects.filter(user=self.request.user)[0] 
		serializer.save(mess=adminmess)


@method_decorator(csrf_exempt, name='dispatch')
class MessAdminCreate(generics.CreateAPIView):
	queryset = MessModel.objects.all()
	serializer_class = MessAdminSerializer
	permission_classes = [
	    permissions.AllowAny
	]
	def perform_create(self, serializer):
		serializer = MessAdminSerializer(data=self.request.data)
		if serializer.is_valid():
			user_form = serializer.save()
			username = serializer.validated_data['username']
			user = get_user_model().objects.get(username=username)
			user_token = Token.objects.get_or_create(user=user)
			user_token = user_token[0]
			user_token = user_token.key
			print('na the key br this '+user_token)
			return Response({'key': user_token}, status=status.HTTP_201_CREATED)
		else:
			context = {'code' : 'error', 'response' : serializer.errors}
			return JsonResponse(context)



class MyProducts(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ProductsSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated, permissions.IsAdminUser
	]
	def get_queryset(self):
		adminmess = MessModel.objects.filter(user=self.request.user)[0]
		qs = Products.objects.all().filter(mess = adminmess)
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
		adminmess = MessModel.objects.filter(user=self.request.user)[0]
		qs = Products.objects.filter(mess = adminmess)
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
		adminmess = MessModel.objects.filter(user=self.request.user)[0]
		qs = Products.objects.filter(mess = adminmess, id=id)
		return qs

class MyMessProfile(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = MessAdminSerializer
	pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.IsAuthenticated, permissions.IsAdminUser
	]
	def get_queryset(self):
		qs = MessModel.objects.filter(user=self.request.user)[0]
		if qs:
			return qs
		else:
			context = {'error' : 'you are not a mess admin'}
			return JsonResponse(context)
