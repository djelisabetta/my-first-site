from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='domanda')
    pub_date = models.DateTimeField('data pubblicazione')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # ritorna un booleano
        # es. 1 restituisce true se >= la data di ieri
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        # es. 2 restituisce true se >= la data di ieri e <= la data di oggi
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='scelta')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
