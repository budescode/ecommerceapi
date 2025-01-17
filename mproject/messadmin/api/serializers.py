from rest_framework import serializers
from products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		exclude = []
		depth = 1

class ProductsCreateSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Products
        exclude = ['user']

        #fields = '__all__'
        # read_only_fields = ('user', )