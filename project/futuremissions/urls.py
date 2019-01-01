from django.conf.urls import url
from futuremissions.views import FuturemissionsView
from . import views

urlpatterns = [
	url(r'^$', FuturemissionsView.as_view(), name='home'),
]