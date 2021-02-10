from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Link
# Create your views here.

def index(request):
	links = Link.objects.all()
	paginator = Paginator(links, 3)
	page = request.GET.get('page')
	paged_links = paginator.get_page(page)
	context = {
		'links' : paged_links
	}
	return render(request, 'links/links.html', context)

def link(request):
	return render(request, 'links/link.html')

