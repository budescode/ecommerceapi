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
            print('na the key br this '+user_token)
            return Response({'key': user_token}, status=status.HTTP_201_CREATED)
        else:
            context = {'code' : 'error', 'response' : serializer.errors}
            return JsonResponse(context)
