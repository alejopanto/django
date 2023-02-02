import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Una pregunta futura", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the past """
        time = timezone.now() - datetime.timedelta(days=1)
        past_question = Question(question_text="Una pregunta del pasado", pub_date=time)
        self.assertFalse(past_question.was_published_recently())

    def test_was_published_recently_with_now_questions(self):
        """was_published_recently returns True for questions whose pub_date is this moment """
        time = timezone.now()
        question_now = Question(question_text="Una pregunta actual", pub_date=time)
        self.assertIs(question_now.was_published_recently(), True)