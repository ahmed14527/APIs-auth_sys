from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('change-password/', views.PasswordChangeAPIView.as_view(), name='change_password'),
    path('password-reset/', views.PasswordResetAPIView.as_view(), name='password_reset'),
    path('password-reset-confirm/', views.PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
    
    
]