"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import (
    include,
    path,
    re_path,
)
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from . import views

favicon_files = [
    'favicon-57.png',
    'favicon-120.png',
    'favicon-152.png',
    'favicon-167.png',
    'favicon-180.png',
    'favicon-192.png',
    'favicon-512.png',
    'favicon-813.png',
    'favicon.ico',
    'favicon.png',
]

favicon_patterns = [
    path(
        filename,
        RedirectView.as_view(url=staticfiles_storage.url(f'favicons/{filename}'))
    )
    for filename in favicon_files
]

urlpatterns = [
    path('', views.index, name='homepage'),
    path('resume/', views.resume, name='resume'),
    path('blog/', include('blog.urls')),
    path('music/', include('music.urls')),
    path('admin/', admin.site.urls),

    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    *favicon_patterns,
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
