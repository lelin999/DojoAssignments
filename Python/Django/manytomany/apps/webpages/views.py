from django.shortcuts import render, redirect
from .models import User, Interest
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request, 'webpages/index.html')

def processview(request):
	return redirect('/display')

def processcreate(request):
	if request.method == 'POST':
		if User.objects.validate(request.POST)[0] == True:
			return redirect('/display')
		else:
			messages.warning(request, User.objects.validate(request.POST)[1])
			return redirect('/')

def display(request):
	return render(request, 'webpages/display.html')

def interests(request):
	return render(request, 'webpages/interests.html')