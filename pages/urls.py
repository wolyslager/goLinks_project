from django.urls import path
from . import views


urlpatterns = [
	path('home', views.home, name="home"),
	path('add', views.add, name='add'),
	path('edit', views.edit, name="edit"),
	path('delete', views.delete, name='delete'),
	path('links', views.links, name = 'links')
]