from django.http import (
    FileResponse,
    HttpResponse,
)
from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        'title': 'BryanHadro.com - Homepage',
    }
    return render(request, 'website/index.html', context)

def resume(request):
    return FileResponse(open(f'{settings.STATIC_ROOT}Bryan_Hadro_Resume.pdf', 'rb'))