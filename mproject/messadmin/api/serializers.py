from rest_framework import serializers
from products.models import Products
from messadmin.models import MessRules, MessModel
from django.contrib.auth import get_user_model

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		exclude = []

class MessRulesSerializer(serializers.ModelSerializer):
	class Meta:
		model = MessRules
		exclude = ['mess']

class MessAdminSerializer(serializers.ModelSerializer):
	username = serializers.CharField()
	password = serializers.CharField()
	email = serializers.EmailField()
	date_of_birth = serializers.DateField()
	# user = serializers.ReadOnlyField(source='user.username')
	class Meta:
		model = MessModel
		exclude = ['user']
		# fields = '__all__'
		# read_only_fields = ('user', )

	def validate_username(self, value):
		qs = get_user_model().objects.filter(username = value)
		if qs.exists():
			raise serializers.ValidationError('username already exist')
		return value
	def validate_email(self, value):
		qs = get_user_model().objects.filter(email=value)
		if qs.exists():
			raise serializers.ValidationError('email already exist')
		return value

	def create(self, validated_data):
		user = get_user_model().objects.create_user(
		username=validated_data['username'],
		email=validated_data['email'],
		date_of_birth = validated_data['date_of_birth'],
		is_staff = True
		)
		user.set_password(validated_data['password'])
		user.save()
		MessModel.objects.create(
		user=user,
		name = validated_data['name'],
		address = validated_data['address'],
		number = validated_data['number'],
		active = False
		)

		return user

class ProductsCreateSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Products
        exclude = ['mess']

        #fields = '__all__'
        # read_only_fields = ('user', )