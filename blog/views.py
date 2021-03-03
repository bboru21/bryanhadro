from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'BryanHadro.com - Blog',
    }
    return render(request, 'blog/index.html', context)
