# pylint: disable=no-member
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html')
