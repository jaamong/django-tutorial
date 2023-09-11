import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)  #  Field is an abstract class that represents a database table column
    pub_date = models.DateTimeField("date published")  # DateTimeField : 날짜와 시간(datetime) 필드 표현

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
