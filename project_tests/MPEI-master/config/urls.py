"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import ( handler404, handler500 )

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about/', include('about_university.urls')),
    path('ads/', include('ads.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('base.urls')),
    path('edu/', include('education.urls')),
    path('news/', include('news.urls')),
    path('science-and-innovations/', include('science_and_innovation.urls')),
    path('in-f/', include('foreign.urls')),
    path('university/', include('university_life.urls')),
    path('structure/', include('structure.urls')),
    path('teachers/', include('teachers.urls')),
    path('data/', include('Document.urls')),

)
handler404 = "base.views.page_not_found_view"
# handler500 = "base.views.custom_error_view"
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
