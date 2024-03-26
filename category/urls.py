from django.urls import path,include
from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('view_set', CategoryViewSet, basename='view_set')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]