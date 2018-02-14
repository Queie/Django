from django.shortcuts import render
# Create your views here.

def home(request):
	context = locals()
	template = "profiles/home.html"
	return render(request, template, context)

def about(request):
	context = locals()
	template = "profiles/about.html"
	return render(request, template, context)