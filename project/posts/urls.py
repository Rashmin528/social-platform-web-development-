from django.conf.urls import url
from posts.views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
)
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='list'),
	url(r'^create/$', views.post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
]