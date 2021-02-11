from django.urls import path
from . import views


urlpatterns = [
	path('<str:link>', views.go, name="go"),
	path('', views.redir, name="redir")
]