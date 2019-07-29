import unittest
from django.urls import reverse
from django.test import Client
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_question(**kwargs):
    defaults = {}
    defaults["Model"] = "Model"
    defaults["name"] = "name"
    defaults["Option1"] = "Option1"
    defaults["Option2"] = "Option2"
    defaults["Option3"] = "Option3"
    defaults["Option4"] = "Option4"
    defaults.update(**kwargs)
    return Question.objects.create(**defaults)


class QuestionViewTest(unittest.TestCase):
    '''
    Tests for Question
    '''
    def setUp(self):
        self.client = Client()

    def test_list_question(self):
        url = reverse('WebApp_question_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_question(self):
        url = reverse('WebApp_question_create')
        data = {
            "Model": "Model",
            "name": "name",
            "Option1": "Option1",
            "Option2": "Option2",
            "Option3": "Option3",
            "Option4": "Option4",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_question(self):
        question = create_question()
        url = reverse('WebApp_question_detail', args=[question.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_question(self):
        question = create_question()
        data = {
            "Model": "Model",
            "name": "name",
            "Option1": "Option1",
            "Option2": "Option2",
            "Option3": "Option3",
            "Option4": "Option4",
        }
        url = reverse('WebApp_question_update', args=[question.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


