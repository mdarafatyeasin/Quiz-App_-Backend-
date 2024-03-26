from django.contrib import admin
from .models import PresentAddress, PermanentAddress, UserInfo

# Register your models here.
admin.site.register(PresentAddress)
admin.site.register(PermanentAddress)
admin.site.register(UserInfo)