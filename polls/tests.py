# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question


# Create your tests here.

# a separate TestClass for each model or view
# a separate test method for each set of conditions you want to test
# test method names that describe their function
# If you can’t test a piece of code, it usually means that code should be refactored or removed.

class QuestionMethodTest(TestCase):
    """
    python manage.py test polls looked for tests in the polls application
    it found a subclass of the django.test.TestCase class
    it created a special database for the purpose of testing
    it looked for test methods - ones whose names begin with test
    """

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_passed_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


def create_question(question_text, days):
    """
    Creates a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionViewTest(TestCase):
    def test_index_page_without_data(self):
        response = self.client.get(reverse('polls:index'))
        self.assertIs(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_with_a_past_question(self):
        create_question("past Question", -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], [
                '<Question: past Question>'
            ]
        )

    def test_index_with_a_future_question(self):
        create_question("future question", 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], []
        )
        self.assertContains(response, "No polls are available.")

    def test_index_with_future_and_past_question(self):
        create_question("future question", 30)
        create_question("past question", -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: past question>'])

    def test_index_with_two_past_question(self):
        create_question("past question", -20)
        create_question("long past question", -100)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [
            '<Question: past question>', '<Question: long past question>'
        ])


class DetailViewTest(TestCase):
    def test_detail_view_with_future_question(self):
        future_question = create_question('future question', 20)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_past_question(self):
        past_question = create_question('past question', -20)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.question_text)
