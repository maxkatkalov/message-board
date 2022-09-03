from django.db import models
from django.db import models


class Post(models.Model):  # new
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Msg(models.Model):  # new
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
