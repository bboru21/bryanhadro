from django.shortcuts import render

from .models import Category


def index(request):
    context = {
        'title': 'BryanHadro.com - Music',
        'categories': Category.objects.all(),
    }
    return render(request, 'music/index.html', context)
