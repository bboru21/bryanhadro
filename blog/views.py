from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render,
)
from .models import Post

def index(request):

    posts = Post.objects.all()
    context = {
        'title': 'BryanHadro.com - Blog',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def post(request, year, month, day, urlname):
    post = get_object_or_404(Post, urlname=urlname)

    context = {
        'title': f'BryanHadro.com - Blog: {post.title}',
        'post': post,
        'keywords': [category.lower() for category in post.categories.all().values_list('name', flat=True)],
    }
    return render(request, 'blog/post.html', context)
