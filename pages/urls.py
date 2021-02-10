from django.urls import path

from . import views

urlpatterns = [
	path('', views.login, name="login"),
	path('register', views.register, name='register'),
	path('home', views.home, name="home"),
	path('add', views.add, name='add'),
	path('edit', views.edit, name="edit"),
	path('delete', views.delete, name='delete'),
	path('view', views.view, name="view")
]