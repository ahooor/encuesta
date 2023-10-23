from django.db import models


class Topic(models.Model):
    topic_name = models.CharField(max_length=50)

    def __str__(self):
        return self.topic_name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    topic = models.ManyToManyField(Topic, related_name='topic', blank=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
    

class Result(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
