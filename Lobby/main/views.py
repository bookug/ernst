#coding:utf-8 

from django.shortcuts import render
from .models import User, Room, Action
from django import forms
from django.http import *
from os import listdir
import os
#NOTICE: avoid import * because functions may be overrided
#there is an open function in os accepting integer args, which conflicts with open in python

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

global active_user
active_user = User()
#global active_room
#active_room = Room()
#global active_action
#active_action = Action()

#TODO: how to manage several connections(update when change)

# Create your views here.
def initialize(request):		#delete all rooms and users, better to be placed in __init.py
	for user in User.objects.all():
		user.delete()
	for room in Room.objects.all():
		room.delete()
	return render(request, 'main/index.html', {'message':"Initialization done!"})

def exit(request):
	global active_user
	try:
		if active_user.room.id != 0:
			for user in Room.objects.filter(id=active_user.room.id):
				user.room = 0
				user.save()
			active_user.room.delete()
	except Exception, e:
		print e
	finally:
		print active_user.nickName
		active_user.delete()
	return render(request, 'main/index.html')

class UserForm(forms.Form):
	nickname = forms.CharField()
	headimg = forms.FileField()

def handle_uploaded_file(f):
	file_name = ""
	try:
		path = "./data/"	#time.strftime('/%Y/%m/%d/%H/%M/%S/')
		if not os.path.exists(path):
			os.makedirs(path)
		file_name = path + f.name
		dest = open(file_name, "wb+")
		for chunk in f.chunks():
			dest.write(chunk)
		dest.close()
	except Exception, e:
		print e
	return file_name

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()

def upload(request):	#only when POST and enctype in <form>
	print request.method
	if request.method == "POST":		#not use != here, not instead
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			form = UploadFileForm()
			return render(request, 'main/upload.html', {'message':"upload successfully!", 'form':form})
		else:
			print "not valid!"
	print "not post!"
	form = UploadFileForm()
	return render(request, 'main/upload.html', {'form':form})

def basic_download(request):			#just for small file
	with open("./data/index.jpg", "rb") as f:	#instead of try-finally, including close()
		c = f.read()
	return HttpResponse(c)

def good_download(request):			#to download big file
	#TODO:How can we download several files one time, how to return?
	file = request.POST.get('file')
	#print file
	def file_iterator(file_name, chunk_size=512):
		f = open(file_name, "rb")
		while True:
			#read() will get the whole file, maybe too large!
			c = f.read(chunk_size)
			if c:
				yield c
			else:
				break
		f.close()
	#for file in file_list:
	if not file:
		print "no file selected, using default!"
		file = "index.jpg"
	this_file_name = "./data/" + file
	#print this_file_name
	response = StreamingHttpResponse(file_iterator(this_file_name))
	#below is used to avoid displaying in web-page
	response['Content-Type'] ='application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="{0}"'.format(this_file_name)
	return response

def download(request):
	file_list = listdir("./data/")
	#print "file_list: ", file_list
	return render(request, 'main/download.html', {'file_list':file_list})

def index(request):
	global active_user
	#ret = request.POST.get('nickname')
	if not request.method == "POST":
		#print "aa, no data!"
		uf = UserForm()
		return render(request, 'main/index.html', {'uf':uf})
	else:		#if request.method == "POST"
		#print "aa, in data!"
		uf = UserForm(request.POST, request.FILES)
		if not uf.is_valid():
			return render(request, 'main/index.html', {'uf':uf, 'message':"invalid name or file!"})
		#handle_uploaded_file(request.FILES['headimg'])
		nickname = request.POST['nickname']
		#headimg = uf.headimg
		headimg = uf.cleaned_data['headimg']
		if User.objects.filter(nickName=nickname):
			uf = UserForm()
			return render(request, 'main/index.html', {'uf':uf, 'message':"this name is used, please input another one!"})
		#add to database
		active_user = User(nickName=nickname, headImg=headimg)
		active_user.save()
		print "aa, save successfully!"
		#print active_user.id
		action_list = Action.objects.all()
		context = {'uf':uf, 'user':active_user, 'action_list':action_list}
		return render(request, 'main/prepare.html', context)

def invite(request):
	#global active_action
	#global active_room
	global active_user
	action_id = request.POST.get('activity')
	room_name = request.POST.get('room_name')
	#print action_id
	active_action = Action.objects.get(id=action_id)
	#print active_action.actNum
	active_room = Room(roomName=room_name, act=active_action, roomSize=active_action.actNum)
	active_room.save()
	active_user.room = active_room
	active_user.save()
	print active_user.nickName
	user_list = User.objects.filter(room=0)
	user_num = active_action.actNum - 1
	context = {'user_list':user_list, 'user_num':user_num}
	return render(request, 'main/invite.html', context)

def play(request):
	global active_user
	user_id_list = request.POST.getlist('user')
	user_list = []
	for each in user_id_list:
		user = User.objects.get(id=each)
		user.room = active_user.room
		user.save()
		print user.nickName
		user_list.append(user)
	user_list.append(active_user)
	#include all information in context
	#print active_user.room.act.id
	act_url = "%s%d%s"%("/act/", active_user.room.act.id, "/")
	context = {'act_url':act_url, 'user_list':user_list, 'room':active_user.room, 'activity':active_user.room.act}
	return render(request, 'main/play.html', context)

