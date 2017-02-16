from django.shortcuts import render, HttpResponse
import datetime, time
# Create your views here.
def index(req):
  context = {
  "somekey": datetime.date.today(),
  "someotherkey": time.strftime("%H:%M")
  }
  return render(req, 'timedisplay/index.html', context)