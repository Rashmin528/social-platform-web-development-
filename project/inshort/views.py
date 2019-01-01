from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

class InshortView(TemplateView):
	template_name = 'temp/inshort.html'

	def inshort(request):
		return render(request, self.template_name, args)


