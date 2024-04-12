from django.http import JsonResponse
import requests
from django.contrib.auth.models import User
from authentication.models import UserInfo
from rest_framework.response import Response
from rest_framework.views import APIView


class userProfile(APIView):
    def get(self, request, id, token):
        authentication_response = requests.get(f'http://127.0.0.1:8000/hook/is_verified/{id}/{token}')

        if authentication_response.status_code == 200:
            user = User.objects.get(id=id)
            user_info = UserInfo.objects.get(user=user)
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number':user_info.phone_number,
                'profile_picture':user_info.profile_picture.url,
            }
            return Response(user_data)
        else:
            print('not verified')
            return JsonResponse({'error': 'Unable to fetch user profile'}, status=authentication_response.status_code)
    


# for change password
# https://medium.com/@thegbolahanalaba/change-password-in-django-rest-framework-d91a71cd0c63
    
