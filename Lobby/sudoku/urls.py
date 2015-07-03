from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^index/', views.index, name='index'),
		url(r'^initialize/', views.initialize, name='initialize'),
		url(r'^play/', views.play, name="play"),
		url(r'^check/', views.check, name="check"),
		url(r'^answer/', views.answer, name="answer"),
		]

