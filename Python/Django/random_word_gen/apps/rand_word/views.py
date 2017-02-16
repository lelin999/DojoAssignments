from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(req):
	if 'num' not in req.session:
		req.session['num'] = 1
	if req.session['num'] > 0:
		req.session['unique_id'] = get_random_string(length=14)
	return render(req, 'rand_word/index.html')

def generate(req):
	if req.method == 'POST':
		req.session['num'] += 1
	return redirect('/')