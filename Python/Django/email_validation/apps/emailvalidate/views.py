from django.shortcuts import render, redirect, HttpResponse
from .models import Email
from django.contrib import messages
# Create your views here.
def index(req):
	return render(req, 'emailvalidate/index.html')

def process(req):
	if req.method == 'POST':
		email = Email.objects.login(req.POST['email'])
		if email == True:
			Email.objects.create(email=req.POST['email'])
			return redirect('/success')
		else:
			# display flash message
 			messages.warning(req, 'Invalid Email!')
			return redirect('/')

def success(req):
	context = {
		"emails": Email.objects.all()
	}
	return render(req, 'emailvalidate/success.html', context)