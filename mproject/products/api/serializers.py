from rest_framework import serializers
from products.models import Products, Categories
from django.contrib.auth import get_user_model


class CategoriesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categories
		exclude = []
		depth = 1


class ProductListSerializer(serializers.ModelSerializer):
	category = CategoriesListSerializer(read_only=True)
	class Meta:
		model = Products
		exclude = ['user']
		depth = 1