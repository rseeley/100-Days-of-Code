from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.text import Truncator


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(
            topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board,
        related_name='topics',
        on_delete=models.CASCADE
    )
    starter = models.ForeignKey(
        User,
        related_name='topics',
        on_delete=models.SET(get_sentinel_user)
    )
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.SET(get_sentinel_user)
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        related_name='+',
        on_delete=models.SET(get_sentinel_user)
    )

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
