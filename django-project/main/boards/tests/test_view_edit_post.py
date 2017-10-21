from django.contrib.auth.models import User
from django.test import TestCase
from django.url import reverse

from ..models import Board, Post, Topic
from ..views import PostUpdateView


class PostUpdateViewTestCase(TestCase):
    """
    Base test case to be used in all `PostUpdateView` view tests
    """

    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django board')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(
            username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(
            subject='Hello, world!', board=self.board, starter=user)
        self.post = Post.objects.create(
            message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)
        self.url = reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })
