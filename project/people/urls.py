from django.conf.urls import url
from people.views import (
	posts_home,
	posts_nikola,
	posts_Gravitational_waves,
	posts_neutrino,
	posts_Wormhole,
	posts_stringtheory,
	posts_einstein,
	posts_bigbang,
	posts_cosmology,
	posts_jupitar,
	posts_fourthdim,
	posts_titan,
	posts_faraday,
	posts_regulus,
	posts_nebula,
	posts_sirius,
)
from . import views

urlpatterns = [
	url(r'^$', views.posts_home, name='home'),
	url(r'^nikola/$', views.posts_nikola, name='nikola'),
	url(r'^Gravitational_waves/$', views.posts_Gravitational_waves, name='Gravitational_waves'),
	url(r'^neutrino/$', views.posts_neutrino, name='neutrino'),
	url(r'^Wormhole/$', views.posts_Wormhole, name='Wormhole'),
	url(r'^stringtheory/$', views.posts_stringtheory, name='stringtheory'),
	url(r'^einstein/$', views.posts_einstein, name='einstein'),
	url(r'^bigbang/$', views.posts_bigbang, name='bigbang'),
	url(r'^cosmology/$', views.posts_cosmology, name='cosmology'),
	url(r'^jupitar/$', views.posts_jupitar, name='jupitar'),
	url(r'^fourthdim/$', views.posts_fourthdim, name='fourthdim'),
	url(r'^titan/$', views.posts_titan, name='titan'),
	url(r'^faraday/$', views.posts_faraday, name='faraday'),
	url(r'^regulus/$', views.posts_regulus, name='regulus'),
	url(r'^nebula/$', views.posts_nebula, name='nebula'),
	url(r'^sirius/$', views.posts_sirius, name='sirius'),
]