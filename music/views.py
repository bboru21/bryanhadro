from django.shortcuts import render

from .models import Category


def index(request):
    categories = Category.objects \
        .filter(primary=True) \
        .exclude(songs__isnull=True)

    context = {
        'title': 'BryanHadro.com - Music',
        'categories': categories,
    }
    return render(request, 'music/index.html', context)
