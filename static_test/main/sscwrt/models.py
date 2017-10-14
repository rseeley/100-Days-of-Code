from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=30, unique=True)
    body = models.RichText()
    url = models.SlugField(max_length=30)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    title = models.CharField(max_length=30, unique=True)
    file = models.FileField()

    def __str__(self):
        return self.title
