from django.db import models
from category.models import questionCategory

# constructor 
QUESTION_LEVEL = [
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
]

# Create your models here.
class QuizCard(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return (self.title)

class QuestionDetail(models.Model):
    quizCard = models.ForeignKey(QuizCard, on_delete = models.CASCADE)
    question_category = models.ForeignKey(questionCategory, on_delete = models.CASCADE, null=True, blank=True)
    question_level = models.CharField(choices = QUESTION_LEVEL, max_length = 20)
    point = models.IntegerField(default=1,)
    question = models.CharField(max_length = 200)
    option1 = models.CharField(max_length = 100)
    option2 = models.CharField(max_length = 100)
    option3 = models.CharField(max_length = 100)
    option4 = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)

    def __str__(self):
        return (self.question_category.categoryName)