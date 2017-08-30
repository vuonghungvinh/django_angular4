from django.shortcuts import render

# Create your views here.

def individual(request):
	return render(request, "dashboard/individual.html", {})

def business(request):
	return render(request, "dashboard/business.html", {})
