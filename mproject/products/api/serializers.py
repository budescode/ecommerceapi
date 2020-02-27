from rest_framework import serializers
from products.models import Products


class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		exclude = ['user']
