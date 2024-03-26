from django.shortcuts import render
from rest_framework import viewsets

from .models import questionCategory
from .serializers import questionCategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = questionCategory.objects.all()
    serializer_class = questionCategorySerializer

# get all the category
class get_category(viewsets.ModelViewSet):
    queryset = questionCategory.objects.all()
    serializer_class = questionCategorySerializer