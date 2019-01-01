from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

class AstronomykidsView(TemplateView):
	template_name = 'temp/astronomykids.html'

	def Astronomykids(request):
		return render(request, self.template_name, args)

class ModelView(TemplateView):
	template_name = 'temp/model.html'

	def Model(request):
		return render(request, self.template_name, args)

class BookView(TemplateView):
	template_name = 'temp/book.html'

	def Book(request):
		return render(request, self.template_name, args)