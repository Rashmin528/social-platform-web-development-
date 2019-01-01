"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.login_redirect, name = 'login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^api/posts/', include('posts.api.urls')),
    url(r'^api/comments/', include('comments.api.urls')),
    url(r'^account/', include('sirius.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^people/', include('people.urls')),
    url(r'^inshort/', include('inshort.urls')),
    url(r'^future-missions/',include('futuremissions.urls')),
    url(r'^astronomy-kids/',include('astronomykids.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
