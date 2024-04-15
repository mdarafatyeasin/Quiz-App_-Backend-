from django.urls import path
from .views import isAuthenticated,isAdmin


urlpatterns = [
    path('is_verified/<int:id>/<token>', isAuthenticated),
    path('is_admin/<int:id>', isAdmin),
]
