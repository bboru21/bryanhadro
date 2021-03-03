from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'BryanHadro.com - Homepage',
    }
    return render(request, 'website/index.html', context)