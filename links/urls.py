from django.urls import path

from . import views

urlpatterns = [
	path('', views.links, name='links'),
	path('<int:link_id>', views.link, name="link")
]