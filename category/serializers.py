from rest_framework import serializers
from .models import questionCategory


class questionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = questionCategory
        fields = "__all__"
