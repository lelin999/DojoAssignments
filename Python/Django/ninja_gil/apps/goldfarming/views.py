from django.shortcuts import render, redirect
import random
# context = {
# 	'gilfromfarm': 0,
# 	'gilfromcave': 0,
# 	'gilfromhouse': 0,
# 	'gilfromcasino': 0
# }

def index(req):
	if 'gil' not in req.session:
		req.session['gil'] = 0
	return render(req, 'goldfarming/index.html')

def process(req):
	if req.method == 'POST':
		if 'activity' not in req.session:
			req.session['activity'] = ''
		if req.POST['building'] == 'farm':
			gil_earned = random.randrange(10,21)
			req.session['gil'] += gil_earned
		if req.POST['building'] == 'cave':
			gil_earned = random.randrange(5,11) 
			req.session['gil'] += gil_earned
		if req.POST['building'] == 'house':
			gil_earned = random.randrange(2,6) 
			req.session['gil'] += gil_earned
		if req.POST['building'] == 'casino':
			gil_earned = random.randrange(-50,51) 
			req.session['gil'] += gil_earned
		if gil_earned >= 0:
			req.session['activity'] += 'Earned {} from {} \n'.format(gil_earned, req.POST['building'])
		else:
			req.session['activity'] += 'Lost {} from {}. Unlucky! \n'.format(gil_earned, req.POST['building'])
		return redirect('/')