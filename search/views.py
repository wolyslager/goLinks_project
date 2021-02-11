from django.shortcuts import render, redirect
from links.models import Link
from django.contrib import messages

# Create your views here.

def go(request, link):
	#check if the golink exists
	#if it does, then pull the url from the database
	#update the number of visits for a golink here
	#if it does not exist, redirect to a page saying the provided link does not exist
	if request.user.is_authenticated:
		goLinkExists = Link.objects.all().filter(golink = link)
		if goLinkExists :
			linkObj = Link.objects.get(golink = link)
			#update the visit count for the golink
			linkObj.visitors = linkObj.visitors + 1
			linkObj.save()
			return redirect(linkObj.url)
		else:
			messages.error(request, 'That go/Link does not exist')
			return redirect('http://localhost:8000/pages/home')

	else:
		return redirect('http://localhost:8000/pages/home')

def redir(request):
	#check if the golink exists
	#if it does, then pull the url from the database
	#if it does not exist, redirect to a page saying the provided link does not exist
	if request.user.is_authenticated:
		return redirect('pages/home')
	else:
		return redirect('http://localhost:8000/users/login')