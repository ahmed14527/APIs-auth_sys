from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.account.views import ConfirmEmailView
from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from django.contrib.auth import get_user_model
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView,
)
from dj_rest_auth.registration.serializers import RegisterSerializer
from .serializers import (
    SignupSerializer,
    LoginSerializer,
    ChangePasswordSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer
)



class SignupAPIView(generics.CreateAPIView):
    """
    View for user registration.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        serializer.save(request=self.request)

class LoginAPIView(LoginView):
    """
    View for user login.
    Inherits from dj_rest_auth's LoginView.
    """

class LogoutAPIView(LogoutView):
    """
    View for user logout.
    Inherits from dj_rest_auth's LogoutView.
    """

class PasswordChangeAPIView(PasswordChangeView):
    """
    View for changing password.
    Inherits from dj_rest_auth's PasswordChangeView.
    """

class PasswordResetAPIView(PasswordResetView):
    """
    View for initiating password reset process.
    Inherits from dj_rest_auth's PasswordResetView.
    """

class PasswordResetConfirmAPIView(PasswordResetConfirmView):
    """
    View for confirming password reset process.
    Inherits from dj_rest_auth's PasswordResetConfirmView.
    """
