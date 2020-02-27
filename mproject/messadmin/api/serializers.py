from rest_framework import serializers
from products.models import Products
from django.contrib.auth import get_user_model

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		exclude = []

class ProductsCreateSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Products
        exclude = []

        #fields = '__all__'
        # read_only_fields = ('user', )