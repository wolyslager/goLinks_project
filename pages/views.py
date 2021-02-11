from django.shortcuts import render, redirect

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return render(request, 'pages/home.html')
	else:
		return redirect('http://localhost:8000/users/login')

def add(request):
	if request.user.is_authenticated:
		return render(request, 'pages/add-link.html')
	else:
		return redirect('http://localhost:8000/users/login')

def edit(request):
	if request.user.is_authenticated:
		return render(request, 'pages/edit-link.html')
	else:
		return redirect('http://localhost:8000/users/login')

def delete(request):
	if request.user.is_authenticated:
		return render(request, 'pages/delete-link.html')
	else:
		return redirect('http://localhost:8000/users/login')

def links(request):
	if request.user.is_authenticated:
		return render(request, 'links/links.html')
	else:
		return redirect('http://localhost:8000/users/login')

def go(request, link):
	#check if the golink exits
	#if it does, then pull the url from the database
	#if it does not exist, redirect to a page saying the provided link does not exist
	if request.user.is_authenticated:
		return redirect('https://www.google.com')
	else:
		return redirect('http://localhost:8000/users/login')


