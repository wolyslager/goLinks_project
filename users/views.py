from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

#Display registration form, validate user input, create new user, log user in
def register(request):
	if request.method == 'POST':
		#form values
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		#password validation
		if password == password2:
			#username validation
			if User.objects.filter(username = username).exists():
				messages.error(request, 'The username is not available')
				return redirect('register')
			else:
				#email validation
				if User.objects.filter(email = email).exists():
					messages.error(request, 'The email is not available')
					return redirect('register')
				else:
					print(firstname)
					user = User.objects.create_user(first_name = firstname, last_name = lastname,
						username = username,email = email, password = password)
					#login
					auth.login(request, user)
					return redirect('http://localhost:8000/home')
					user.save()
		else:
			messages.error(request, 'Passwords do not match')
			return redirect('register')
	else:
		return render(request, 'users/register.html')

#Display login form, validate user input, log user in
def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username = username, password = password)
		#validate user
		if user is not None:
			auth.login(request, user)
			return redirect('http://localhost:8000/home')
		else:
			messages.error(request, 'Invalid username/password combination')
			return redirect('login')
	else:
		return render(request, 'users/login.html')

#Take user to login page and log user out
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
	return render(request, 'users/login.html')

