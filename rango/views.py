from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	html = "<html><body>Rango says hey there partner! <a href='/rango/about/'>About</a></body></html>"
	return HttpResponse(html)

def about(request):
	html = "<html><body>Rango says here is the about page. <a href='/rango/'>Index</a></body></html>"
	return HttpResponse(html)
