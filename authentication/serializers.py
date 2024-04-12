from rest_framework import serializers
from .models import PresentAddress, PermanentAddress, UserInfo
from django.contrib.auth.models import User


class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentAddress
        fields = '__all__'  # You can also specify individual fields if needed

class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddress
        fields = '__all__'  # You can also specify individual fields if needed

class UserInfoSerializer(serializers.ModelSerializer):
    present_address = PresentAddressSerializer()
    permanent_address = PermanentAddressSerializer()

    class Meta:
        model = UserInfo
        fields = '__all__'  # You can also specify individual fields if needed

# Registration
class userRegistrationSerializer(serializers.ModelSerializer):
    # extra ja ja nite cai ekhane age likhte hobe
    phone_number = serializers.CharField(max_length=15) 
    confirm_password = serializers.CharField(required=True) # User model e kono Confirm_password bolte kichui nai tai eta newa hoyeche
    class Meta:
        model = User
        # amar je je fild gulo user theke nite cai shegulo nibo
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password']

    # eti ekti builtin function ja database e ekti record toiri korbe
    def create(self, validated_data): #is_valid check korbe j shob data valid ki na eta dawa baddhotomulok
        # issa moto     =   j name fild gulo dawa asa upore
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        phone_number = validated_data['phone_number']
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']

        # 2 ti password e check kora hocce ekoi kina
        if password != confirm_password:
            raise serializers.ValidationError({"error": "Password doesn't match"})

        # ekoi e-mail 2 bar bybohar kora hoyeche ki na
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email already exists"})

        # Create User instance
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.is_active = False
        user.save()

        user_info = {'user':user, 'phone_number':phone_number}
        present_address = {'user':user}
        permanent_address = {'user':user}
        
        UserInfo.objects.create(**user_info)
        PresentAddress.objects.create(**present_address)
        PermanentAddress.objects.create(**permanent_address)

        return user


# login serializer
    # model er proyojon nai karon amara eti database e save korci na. just user theke 2 ti value niye database a check kori
class loginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ['username', 'password']

# user update
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']