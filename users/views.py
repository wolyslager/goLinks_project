from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
	if request.method == 'POST':
		#get form values
		firstname = (request.POST.get('firstname'))
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		#check passwords match
		if password == password2:
			#check for username
			if User.objects.filter(username = username).exists():
				messages.error(request, 'The username is not available')
				return redirect('register')
			else:
				#check for email
				if User.objects.filter(email = email).exists():
					messages.error(request, 'The email is not available')
					return redirect('register')
				else:
					#everything checks out, create user
					print(firstname)
					user = User.objects.create_user(first_name = firstname, last_name = lastname,
						username = username,email = email, password = password)
					#login
					auth.login(request, user)
					return redirect('http://localhost:8000/pages/home')
					user.save()
		else:
			messages.error(request, 'Passwords do not match')
			return redirect('register')
	else:
		return render(request, 'users/register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username = username, password = password)

		#if the user exists
		if user is not None:
			auth.login(request, user)
			return redirect('http://localhost:8000/pages/home')
		else:
			messages.error(request, 'Invalid username/password combination')
			return redirect('login')
	else:
		return render(request, 'users/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
	return render(request, 'users/login.html')

