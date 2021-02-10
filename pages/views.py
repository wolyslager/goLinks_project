from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request, 'pages/login/login.html')

def register(request):
	return render(request, 'pages/register/register.html')

def home(request):
	return render(request, 'pages/home/home.html')

def add(request):
	return render(request, 'pages/add-link/add-link.html')

def edit(request):
	return render(request, 'pages/edit-link/edit-link.html')

def delete(request):
	return render(request, 'pages/delete-link/delete-link.html')

def view(request):
	return render(request, 'pages/view-all/view-all.html')