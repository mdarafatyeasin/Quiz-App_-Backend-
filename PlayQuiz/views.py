from rest_framework import viewsets
from .models import QuizCard, QuestionDetail
from .serializers import QuizCardSerializer, QuestionDetailSerializer
from django.http import HttpResponse
from django.http import JsonResponse

# views
class QuizCardViewSet(viewsets.ModelViewSet):
    queryset = QuizCard.objects.all()
    serializer_class = QuizCardSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionDetail.objects.all()
    serializer_class = QuestionDetailSerializer
    
def CardQuestions(request, id):
    card_id = id
    all_question = QuestionDetail.objects.filter(quizCard_id=card_id)

    # Convert queryset to list of dictionaries
    filter_data = list(all_question.values())

    # Return filtered data as JSON response
    return JsonResponse(filter_data, safe=False)