from django.urls import path
from .views import isAuthenticated


urlpatterns = [
    path('is_verified/<int:id>/<token>', isAuthenticated)
]
