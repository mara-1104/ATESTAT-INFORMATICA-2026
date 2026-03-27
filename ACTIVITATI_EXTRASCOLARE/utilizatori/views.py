from django.shortcuts import render

# Create your views here.

def login_view(request):
	context = {}
	return render(request, 'login.html', context)

def logout_view(request):
	context = {}
	return render(request, 'logout.html', context)
