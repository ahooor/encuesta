from django.test import TestCase

from encuesta.models import Question, Answer


class QuestionTest(TestCase):
    def setUp(self):
        Question.objects.create(id=1, question_text="First Question")

    def test_orm(self):
        test_object = Question.objects.get(id=1)
        text = test_object.question_text
        self.assertEqual("Test Question", text)

    def test_update(self):
        test_object = Question.objects.get(id=1)
        test_object.question_text = "Updated text"
        test_object.save()
        updated_object = Question.objects.get(id=1)
        text = updated_object.question_text
        self.assertEqual("Updated text", text)

    def test_delete(self):
        test_object = Question.objects.get(id=1)
        test_object.delete()
        deleted_object = Question.objects.get(id=1)
        self.assertEqual()








# class AnswerTest(TestCase):
#     def setUp(self):
#         Answer.objects.