from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#index view
def index(request):
	"""
	I prefer writing descrption for a view function here inside a function prototype.
	"""
	return HttpResponse("Hello, world. You are at the polls index, Mr.Zhang, congratulations.")
#end of index

