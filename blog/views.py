from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render,
)
from .models import Post
from django.conf import settings

def index(request):

    posts = Post.objects.filter(active=True)
    context = {
        'title': 'BryanHadro.com - Blog',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def post(request, year, month, day, urlname):
    post = get_object_or_404(Post, urlname=urlname, active=True)

    context = {
        'title': f'BryanHadro.com - Blog: {post.title}',
        'post': post,
        'keywords': [category.lower() for category in post.categories.all().values_list('name', flat=True)],
        'url': f'{settings.WEBSITE_URL}{post.url}',
    }
    return render(request, 'blog/post.html', context)
