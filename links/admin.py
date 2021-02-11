from django.contrib import admin

# Register your models here.
from .models import Link

class LinksAdmin(admin.ModelAdmin):
	list_display = ('golink', 'url', 'visitors', 'user')

admin.site.register(Link, LinksAdmin)