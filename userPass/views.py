from django.shortcuts import render
from .serializer import ForgotPasswordSerializer, ResetPasswordSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_password_reset_email(email, reset_link):
    subject = "Password Reset Request"
    message = f"Click the link below to reset your password:\n\n{reset_link}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)



class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            try:
                user = User.objects.get(email=email)
                # print(user)
            except User.DoesNotExist:
                return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
            
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://localhost:5173/login/forgot_password/reset_password/{uidb64}/{token}"
            send_password_reset_email(email, reset_link)
            return Response({"message": "Please check your mail to reset your password", "token":uidb64+'/'+token})
        else:
            # print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# reset password
class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']

            split_token = token.split("/")
            uidb64 = split_token[0]
            token = split_token[1]

            uid = urlsafe_base64_decode(uidb64).decode('utf-8')
            
            try:
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
                # print(e)
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                # print(new_password)  # Check if new_password is correct
                user.set_password(new_password)
                user.save()
                return Response({"message": "Password reset successfully."})
            else:
                # print("Invalid token or user.")
                return Response({"error": "Invalid token or user."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message':'gotit'})

    
 