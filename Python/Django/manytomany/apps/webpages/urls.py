from django.conf.urls import url
from . import views       
urlpatterns = [
  url(r'^$', views.index),
  url(r'^processview$', views.processview),
  url(r'^processcreate$', views.processcreate),
  url(r'^display$', views.display),
  url(r'^interests$', views.interests)
]