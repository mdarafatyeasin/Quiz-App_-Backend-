from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER, ROLE

class PresentAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"Present Address of {self.user.username}"

class PermanentAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"Permanent Address of {self.user.username}"

# main profile 
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    present_address = models.ForeignKey(PresentAddress, on_delete=models.CASCADE, null=True)
    permanent_address = models.ForeignKey(PermanentAddress, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.FileField(upload_to ='account/profile_picture/')
    gender = models.CharField(max_length=10, choices=GENDER)
    role = models.CharField(max_length=10, choices=ROLE)

    def __str__(self):
        return f"User Information for {self.user.username}"
