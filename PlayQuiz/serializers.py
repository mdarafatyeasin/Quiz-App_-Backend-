from rest_framework import serializers
from .models import QuizCard, QuestionDetail


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionDetail
        fields = '__all__'

class QuizCardSerializer(serializers.ModelSerializer):
    # questions = QuestionDetailSerializer(many=True, read_only=True)
    class Meta:
        model = QuizCard
        fields = '__all__'
        # fields = ['id','title','description', 'questions']
