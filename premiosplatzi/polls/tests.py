import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

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


def create_question(question_text, days):
    """Create a question"""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no question exists, and appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay polls.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question(self):
        """if the question is in the future not showing"""
        response = self.client.get(reverse("polls:index"))
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Una pregunta futura", pub_date=time)
        self.assertNotIn(future_question, response.context["latest_question_list"])

    def test_past_question(self):
        """if the question is in the past show in the app"""
        question = create_question("pregunta del pasado", days=-10)
        respose = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(respose.context["latest_question_list"], [question])

    def test_future_question_adn_past_question(self):
        """Only show past question"""
        past_question = create_question("Pregunta del pasado", days=-30)
        future_question = create_question("Pregunta del futuro", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question]
        )

    def test_two_past_questions(self):
        """show all past questions"""
        past_question1 = create_question("Pregunta del pasado 1", days=-30)
        past_question2 = create_question("Pregunta del pasado 2", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question1, past_question2]
        )

    def test_tqo_future_question(self):
        """not show future questions"""
        future_question1 = create_question("Pregunta del futuro 1", days=30)
        future_question2 = create_question("Pregunta del futuro 2", days=40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            []
        )
    

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """ is the question pub_date is in the future, show 404 """
        future_question = create_question("Pregunta del futuro", days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_past_question(self):
        """ is the question is in past, show the text question """
        past_question = create_question("Pregunta del pasado", days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)