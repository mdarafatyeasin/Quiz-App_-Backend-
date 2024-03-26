from django.shortcuts import render,redirect
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import JsonResponse


# Create your views here.
# email confirm_link
def send_confirmation_email(user, confirm_link, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'confirm_link' : confirm_link,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

# registration
class UserRegistration (APIView):
    serializer = serializers.userRegistrationSerializer

    def post(self, request):
        serializer = self.serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid: ", uid)
            print("token: ", token)
            confirm_link = f"http://127.0.0.1:8000/auth/active/{uid}/{token}"
            send_confirmation_email(user,confirm_link, 'Email confirmation', 'confirm_email.html')
            return Response("Check your mail for confirmation")
        
        return Response(serializer.errors)

# confirm email to activate account
def activate(request, uid64, token):
    try: 
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid) 
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

# login 
class userLogin(APIView):
    def post(self,request):
        serializer = serializers.loginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token,_ = Token.objects.get_or_create(user=user)
                print(user)
                return Response({'token': token.key, 'user': {'id': user.id, 'username': user.username}})
                # return Response({'token':token.key, 'user_id':user.id})
            else:
                return Response({'error':'Invalid User'})
        else:
            return Response(serializer.error)

# authenticate
def checkUser(request, id, token):
    try:
        user = User.objects.get(id=id)
        print('User found:', user)

        # Check if the token is associated with the user
        try:
            token_obj = Token.objects.get(user=user, key=token)
            print('Token is valid')
            return JsonResponse({'status': 'success', 'user': {'id': user.id, 'username': user.username}})
        except Token.DoesNotExist:
            print('Token is invalid')
            return JsonResponse({'status': 'error', 'message': 'Invalid token'}, status=401)

    except User.DoesNotExist:
        print('User not found')
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)