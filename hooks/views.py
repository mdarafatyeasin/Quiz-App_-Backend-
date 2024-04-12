from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer  # Import the serializer you created

@api_view(['GET'])
def isAuthenticated(request, id, token):
    try:
        user = User.objects.get(id=id)
        # print('(hooks) User found:', user)

        # Check if the token is associated with the user
        try:
            token_obj = Token.objects.get(user=user, key=token)
            print(user)
            serializer = UserSerializer(user)  # Serialize the user object
            # print(serializer.data)
            return Response(serializer.data)  # Return the serialized user data
        except Token.DoesNotExist:
            print('Token is invalid')
            return Response({'status': 'error', 'message': 'Invalid token'}, status=401)

    except User.DoesNotExist:
        print('User not found')
        return Response({'status': 'error', 'message': 'User not found'}, status=404)
