from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizCardViewSet, QuestionViewSet,CardQuestions

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('quiz_card', QuizCardViewSet, basename='quiz_card')
router.register('all_questions', QuestionViewSet, basename='questions')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('card_question/<int:id>', CardQuestions)
]