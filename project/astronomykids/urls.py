from django.conf.urls import url
from astronomykids.views import (
	AstronomykidsView,
	ModelView,
	BookView,
)
from . import views

urlpatterns = [
	url(r'^$', AstronomykidsView.as_view(), name='home'),
	url(r'^model/$', ModelView.as_view(), name='model'),
	url(r'^book/$', BookView.as_view(), name='book'),
]