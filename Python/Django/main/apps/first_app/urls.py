from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]

print "I will be your future routes: HTTP requests will be captured by me!"