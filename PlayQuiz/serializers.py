from rest_framework import serializers
from .models import QuizCard, QuestionDetail

class QuizCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCard
        fields = '__all__'

class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionDetail
        fields = '__all__'
