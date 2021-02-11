from django.shortcuts import render, redirect

# Create your views here.

def go(request, link):
	#check if the golink exists
	#if it does, then pull the url from the database
	#if it does not exist, redirect to a page saying the provided link does not exist
	if request.user.is_authenticated:
		return redirect('https://www.google.com')
	else:
		return redirect('http://localhost:8000/users/login')

def redir(request):
	#check if the golink exists
	#if it does, then pull the url from the database
	#if it does not exist, redirect to a page saying the provided link does not exist
	if request.user.is_authenticated:
		return redirect('pages/home')
	else:
		return redirect('http://localhost:8000/users/login')