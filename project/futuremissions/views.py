from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

class FuturemissionsView(TemplateView):
	template_name = 'temp/futuremissions.html'

	def Futuremissions(request):
		return render(request, self.template_name, args)



