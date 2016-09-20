from django.conf.urls import url

from . import views #here to refer to polls/views.py

urlpatterns = [url(r'^$', views.index, name = 'index')]

