from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):

    posts = Post.objects.all()
    context = {
        'title': 'BryanHadro.com - Blog',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)
