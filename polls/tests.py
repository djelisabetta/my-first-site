# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # la funzione was_published_recently restituisce true se pub_date è >= la data di ieri,
        # il nostro test è finalizzato a testare che ritorni false anche quando pub_date > data di oggi
        # controlliamo l'output di was_published_recently()- che dovrebbe essere falso.
        self.assertIs(future_question.was_published_recently(), False)