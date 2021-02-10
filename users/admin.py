from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'email')

admin.site.register(User, UserAdmin)