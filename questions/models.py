from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=300, blank=False)
    detail = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.question