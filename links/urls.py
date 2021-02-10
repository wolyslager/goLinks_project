from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='links'),
	path('<int:link_id>', views.link, name="link")
]