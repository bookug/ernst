from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^initialize/', views.initialize, name='initialize'),
		url(r'^exit/', views.exit, name='exit'),
		url(r'^index/', views.index, name='index'),
		url(r'^invite/', views.invite, name='invite'),
		url(r'^play/', views.play, name='play'),
		]

