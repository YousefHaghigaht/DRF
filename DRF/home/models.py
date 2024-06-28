from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.email


class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    tittle = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.tittle}'


class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers')
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} {self.question}'

