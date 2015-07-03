from django.shortcuts import render
from .models import User, Room, Action

global active_user
active_user = User()
#global active_room
#active_room = Room()
#global active_action
#active_action = Action()

#TODO: how to manage several connections(update when change)
#TODO: error when dealing with Chinese characters

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

def index(request):
	global active_user
	ret = request.POST.get('nickname')
	if not ret:
		print "aa, no data!"
		return render(request, 'main/index.html')
	else:
		print "aa, in data!"
		if User.objects.filter(nickName=ret):
			context = {'message':'this name is used, please input another one!'}
			return render(request, 'main/index.html', context)
		#add to database
		active_user = User(nickName=ret)
		active_user.save()
		print "aa, save successfully!"
		#print active_user.id
		action_list = Action.objects.all()
		context = {'user':active_user, 'action_list':action_list}
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

