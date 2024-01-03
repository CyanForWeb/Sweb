from django.conf import settings
from django.db import models
from django.utils import timezone

class Questions(models.Model):
    title = models.TextField(default="null")
    question = models.TextField(default="null")
    image = models.CharField(max_length=2, default="0")
    correct = models.TextField(default="null")
    incorrect_1 = models.TextField(default="null")
    incorrect_2 = models.TextField(default="null")
    incorrect_3 = models.TextField(default="null")
    incorrect_4 = models.TextField(default="null")
    incorrect_5 = models.TextField(default="null")
    discription = models.TextField(default="null")
    def __str__(self):
        return self.question+':'+self.image

class Test(models.Model):
    question_id = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.question_id
