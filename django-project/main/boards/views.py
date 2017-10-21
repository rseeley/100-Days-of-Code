from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from django.utils import timezone

from .forms import NewTopicForm, PostForm
from .models import Board, Topic, Post


def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'home.html', context)


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by(
        '-last_updated').annotate(replies=Count('posts') - 1)
    context = {'board': board, 'topics': topics}
    return render(request, 'topics.html', context)


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()

            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )

            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    context = {'board': board, 'form': form}
    return render(request, 'new_topic.html', context)


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    context = {'topic': topic, 'form': form}
    return render(request, 'reply_topic.html', context)


class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    success_rul = reverse_lazy('post_list')
    template_name = 'new_post.html'


class UpdatePostView(UpdateView):
    model = Post
    fields = ('message',)
    template_name = 'edit_post.html'
    pk_url_kwarg = 'topic_pk'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect(
            'topic_posts',
            pk=post.topic.board.pk,
            topic_pk=post.topic.pk)


# class NewTopicView(View):
#     def __init__(self):
#         self.board = get_object_or_404(Board, pk=self.pk)
#         self.user = User.objects.first()

#     def post(self, request):
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = self.board
#             topic.starter = self.user
#             topic.save()

#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=self.user
#             )

#             return redirect('board_topics', pk=self.board.pk)

#     def get(self, request):
#         form = NewTopicForm()

#     context = {'board': board, 'form': form}
#     return render(request, 'new_topic.html', context)
