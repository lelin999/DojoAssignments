from django.shortcuts import render, HttpResponse

# Create your views here.
def index(req):
	return render(req, 'turtles/index.html')

def all_ninja(req):
	return render(req, 'turtles/ninjas.html')

def one_ninja(req, id):
	context = {
		"id": id
	}
	if context['id'] == 'blue':
		context['id'] = 'Leonardo'
	elif context['id'] == 'orange':
		context['id'] = 'Michelangelo'
	elif context['id'] == 'red':
		context['id'] = 'Raphael'
	elif context['id'] == 'purple':
		context['id'] = 'Donatello'
	else:
		context['id'] = 'Megan Fox'
		# insert links instead of string
	return render(req, 'turtles/specific_ninjas.html', context)
