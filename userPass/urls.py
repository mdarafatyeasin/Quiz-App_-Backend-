from django.urls import path
from .views import ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]
