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
    }
    return render(request, 'website/index.html', context)

def resume(request):
    return FileResponse(open(f'{settings.STATIC_ROOT}/Bryan_Hadro_Resume.pdf?c=20241203', 'rb'))