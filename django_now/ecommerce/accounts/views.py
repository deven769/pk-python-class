from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
# Create your views here.



def signup(request):
	if request.method == 'GET':
		form = SignupForm()
		return render(request, 'accounts/signup.html', {'form':form})
	
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("accounts:login")
		return render(request, 'accounts/signup.html', {'form':form})

def user_login(request):
	if request.method == 'GET':
		form = LoginForm()
		return render(request, 'accounts/login.html', {'form':form})
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		error = ''
		if form.is_valid():
			data = form.cleaned_data
			username = data.get('username')
			password = data.get('password')
			user = authenticate(request, username = username, password = password)
			if user:
				login(request, user)
				return redirect('catalogue:index')
			error = 'Crediential didnt match'
		return render(request, 'accounts/login.html', {'form':form, 'error':error})

