from django.conf.urls import url
from . import views 
urlpatterns = [
  url(r'^$', views.index),
  url(r'^ninjas$', views.all_ninja),
  url(r'^ninjas/(?P<id>[%&+ \w]+)$', views.one_ninja)
]

# ^url/(?P<id> REGEXHERE)$