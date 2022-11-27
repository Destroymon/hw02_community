from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.select_related('author')[:10]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:10]
    template = 'posts/group_list.html'
    context = {
        'text': slug,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
