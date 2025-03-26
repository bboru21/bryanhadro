from django.http import (
    FileResponse,
    HttpResponse,
)
from django.shortcuts import render
from django.conf import settings

from blog.models import Post

def index(request):
    posts = Post.objects.filter(active=True)

    context = {
        'title': 'BryanHadro.com - Homepage',
        'posts': posts[:5],
        'static_root': settings.STATIC_ROOT,
    }
    return render(request, 'website/index.html', context)

def resume(request):
    return FileResponse(open(f'{settings.STATIC_ROOT}/Bryan-Hadro-Resume_2024-12-19.pdf', 'rb'))