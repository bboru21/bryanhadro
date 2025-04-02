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
    response = FileResponse(open(f'{settings.STATIC_ROOT}/Bryan-Hadro_Resume.pdf', 'rb'))
    
    # add headers to prevent caching
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    # add content disposition header for better download handling
    response['Content-Disposition'] = 'inline; filename="Bryan-Hadro_Resume.pdf"'

    return response
