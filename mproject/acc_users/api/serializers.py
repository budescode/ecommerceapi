from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    
    #date_of_birth = serializers.DateField(default="1970-01-01", input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'date_of_birth')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

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
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user