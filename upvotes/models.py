from django.db import models
from django.contrib.auth.models import User
from questions.models import Question


class Upvote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='upvotes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        unique_together = ['owner', 'question']

    def __str__(self):
        return f'{self.owner} {self.question}'