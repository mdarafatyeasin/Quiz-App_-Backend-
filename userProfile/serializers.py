from rest_framework import serializers
from django.contrib.auth.models import User

# user update
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']