from django.shortcuts import render, redirect

context = {
	'name': '',
	'location': '',
	'language': ''
}
# Create your views here.	
def index(req):
	if 'count' not in req.session:
		req.session['count'] = 1
	return render(req, 'form/index.html')

def process(req):
	if req.method == 'POST':
		if req.POST['button'] == 'Go Back':
			return render(req, 'form/index.html')
		else:
			# req.session['count'] += 1
			# req.session['name'] = req.POST['name']
			# req.session['location'] = req.POST['location']
			# req.session['language'] = req.POST['language']
			context['name'] = req.POST['name']
			context['location'] = req.POST['location']
			context['language'] = req.POST['language']
			return redirect('/results')

def results(req):
	return render(req, 'form/results.html', context)