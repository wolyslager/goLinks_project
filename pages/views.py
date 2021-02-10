from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'pages/home.html')

def add(request):
	return render(request, 'pages/add-link.html')

def edit(request):
	return render(request, 'pages/edit-link.html')

def delete(request):
	return render(request, 'pages/delete-link.html')

def links(request):
	return render(request, 'links/links.html')
