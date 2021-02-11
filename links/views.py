from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Link

# Create your views here.

def links(request):
	if request.user.is_authenticated:
		#check if it is a POST request
		if request.method == 'POST':
			print('Hello')
			return
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

