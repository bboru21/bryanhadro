from django.urls import (
    path,
    re_path,
)

from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    re_path(r'(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/(?P<urlname>[a-zA-Z0-9\-]+)$', views.post, name='blog_post')
]