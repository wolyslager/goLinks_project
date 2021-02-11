from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Link
from django.contrib import messages

#Display homepage if user is authenticated
def home(request):
	if request.user.is_authenticated:
		return render(request, 'links/home.html')
	else:
		return redirect('http://localhost:8000/users/login')

#Display go/links page and enable pagination, as well as 
#provide the list of links to be displayed
def links(request):
	if request.user.is_authenticated:
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

#Display add-link form and validate user entries to ensure
#go/link name are not repeated
def add(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			url = request.POST.get('url')
			golink = request.POST.get('golink')
			username = request.POST.get('username')
			goLinkExists = Link.objects.all().filter(golink = golink)
			#validate link
			if goLinkExists:
				messages.error(request, 'The goLink name is already taken')
				return redirect('add')
			link = Link(url = url, golink = golink, user = username, visitors = 0)
			link.save()
			return redirect('home')
		else:
			return render(request, 'links/add-link.html')
	else:
		return redirect('http://localhost:8000/users/login')

#Display edit-link form and validate user entry as well as user
#Enables go/link ownership as only the creator of a link can edit it
def edit(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			new = request.POST.get('new')
			golink = request.POST.get('golink')
			username = request.POST.get('username')
			goLinkExists = Link.objects.all().filter(golink = golink)
			if goLinkExists:
				link = Link.objects.get(golink = golink)
				#validat user
				if link.user == username:
					#validate link
					goLinkExists = Link.objects.all().filter(golink = new)
					if goLinkExists:
						messages.error(request, 'The goLink name is already taken')
						return redirect('edit')
					else:
						link.golink = new;
						link.save()
						return redirect('home')
				else:
					messages.error(request, 'You are not authorized to edit this goLink')
					return redirect('edit')
		else:
			return render(request, 'links/edit-link.html')
	else:
		return redirect('http://localhost:8000/users/login')


#Display delete-link form and validate user entry as well as user
#Enables go/link ownership as only the creator of a link can delete it
def delete(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			golink = request.POST.get('golink')
			username = request.POST.get('username')
			#validate link
			goLinkExists = Link.objects.all().filter(golink = golink)
			if goLinkExists:
				link = Link.objects.get(golink = golink)
				#validate user
				if link.user == username:
					link.delete()
					return redirect('home')
				else:
					messages.error(request, 'You are not authorized to delete this goLink')
					return redirect('delete')
		else:
			return render(request, 'links/delete-link.html')
	else:
		return redirect('http://localhost:8000/users/login')



#Enable go/link functionality by extracting the string parameter entered in the url, 
#validating it, and redirecting the user to the go/link's url 
def go(request, link_param):
	if request.user.is_authenticated:
		goLinkExists = Link.objects.all().filter(golink = link_param)
		if goLinkExists:
			linkObj = Link.objects.get(golink = link_param)
			linkObj.visitors = linkObj.visitors + 1
			linkObj.save()
			return redirect(linkObj.url)
		else:
			messages.error(request, 'That go/Link does not exist')
			return redirect('home')
	else:
		return redirect('home')

#Only display home if user is authenticated
def redir(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		return redirect('http://localhost:8000/users/login')