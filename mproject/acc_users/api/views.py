from rest_framework import generics
from acc_users.api.serializers import UserSerializer
from rest_framework import permissions
from django.db.models import Q
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from acc_users.api.serializers import MessAdminLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate

class MyUserLogin(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = MessAdminLoginSerializer
	#pagination_class = PostLimitOffsetPagination
	permission_classes = [
	    permissions.AllowAny
	]
	def post(self, request, format=None):
		serializer = MessAdminLoginSerializer(data=request.data)
		if serializer.is_valid():
			username = serializer.validated_data['username']
			password = serializer.validated_data['password']
			user = authenticate(username=username, password=password)
			print(user, username, password)
			if user is not None:
				if user.is_active:
					user_token = Token.objects.get_or_create(user=user)
					user_token = user_token[0]
					user_token = user_token.key
					userdetails = {}
					userdetails['username'] = user.username
					userdetails['email'] = user.email
			# 		userdetails['messname'] = messadmin.name
					userdetails['address'] = user.address
			# 		userdetails['messnumber'] = messadmin.number
					userdetails['token'] = user_token
					userdetails['status'] = status.HTTP_200_OK
					return Response(userdetails, status=status.HTTP_200_OK)
				# 	except MessModel.DoesNotExist:
				# 		return Response('you are not a mess admin', status=status.HTTP_404_NOT_FOUND)
			else:
			    userdetails = {'error':'Invalid login details', 'status':status.HTTP_404_NOT_FOUND}
			    return Response(userdetails, status=status.HTTP_404_NOT_FOUND)
	def get_queryset(self):
	    qs = []
	    return qs
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class UserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            user_form = serializer.save()
            user = get_user_model().objects.get(pk=user_form.pk)
            user_token = Token.objects.get_or_create(user=user)
            user_token = user_token[0]
            user_token = user_token.key
            return Response({'key': user_token}, status=status.HTTP_201_CREATED)
        else:
            context = {'code' : 'error', 'response' : serializer.errors}
            return JsonResponse(context)

