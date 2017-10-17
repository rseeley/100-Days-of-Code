from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .forms import NewTopicForm
from .models import Board, Topic, Post


def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'home.html', context)


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {'board': board}
    return render(request, 'topics.html', context)


# @login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    context = {'board': board, 'form': form}
    return render(request, 'new_topic.html', context)


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
