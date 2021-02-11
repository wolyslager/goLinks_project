from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Link
from django.contrib import messages

# Create your views here.

def links(request):
	if request.user.is_authenticated:
		#check if it is a POST request
		if request.method == 'POST':

			#get values from form
			#check which form is being submitted (add, edit, delete)
			if 'add-link' in request.POST:
				url = request.POST.get('url')
				golink = request.POST.get('golink')
				username = request.POST.get('username')
				#check if golink already exists
				goLinkExists = Link.objects.all().filter(golink = golink)
				if goLinkExists:
					messages.error(request, 'The goLink name is already taken')
					return redirect('http://localhost:8000/pages/add')
				#push values into db
				link = Link(url = url, golink = golink, user = username, visitors = 0)
				link.save()
				return redirect('http://localhost:8000/pages/home')

			if 'edit-link' in request.POST:
				new = request.POST.get('new')
				golink = request.POST.get('golink')
				username = request.POST.get('username')
				#check if the golink exists
				goLinkExists = Link.objects.all().filter(golink = golink)
				if goLinkExists:
					#get link
					link = Link.objects.get(golink = golink)
					#check if the user is authorized to edit it
					if link.user == username:
						#get the new value passed by the user
						link.golink = new;
						link.save()
						return redirect('http://localhost:8000/pages/home')
					else:
						messages.error(request, 'You are not authorized to edit this goLink')
						return redirect('http://localhost:8000/pages/edit')

			if 'delete-link' in request.POST:
				golink = request.POST.get('golink')
				username = request.POST.get('username')
				#check if the golink exists
				goLinkExists = Link.objects.all().filter(golink = golink)
				if goLinkExists:
					#get link
					link = Link.objects.get(golink = golink)
					#check if the user is authorized to edit it
					if link.user == username:
						#Delete the goLink
						link.delete()
						return redirect('http://localhost:8000/pages/home')
					else:
						messages.error(request, 'You are not authorized to delete this goLink')
						return redirect('http://localhost:8000/pages/delete')

		user = request.user.username
		links = Link.objects.all()
		paginator = Paginator(links, 3)
		page = request.GET.get('page')
		paged_links = paginator.get_page(page)
		context = {
			'links' : paged_links
		}
		return render(request, 'links/links.html', context)
	else:
		return redirect('http://localhost:8000/users/login')

def link(request):
	if request.user.is_authenticated:
		return render(request, 'links/link.html')
	else:
		return redirect('http://localhost:8000/users/login')

