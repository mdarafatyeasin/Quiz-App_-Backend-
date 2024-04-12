from django.urls import path
from .views import userProfile

urlpatterns = [
    path('<int:id>/<token>', userProfile.as_view(), name='profile')   
]
