from rest_framework import serializers
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		exclude = []
		depth = 1

class CartCreateSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Cart
        exclude = ['user', 'product', 'amount']

        #fields = '__all__'
        # read_only_fields = ('user', )