from django.conf.urls import url
from inshort.views import InshortView
from . import views

urlpatterns = [
	url(r'^$', InshortView.as_view(), name='home'),
]