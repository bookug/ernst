from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
#BETTER: place needed methods here
class Action(models.Model):
	actName = models.CharField(max_length=20, default="")
	actNum = models.IntegerField(default=0)
	def __str__(self):
		return self.actName

class Room(models.Model):
	roomName = models.CharField(max_length=20, default="")
	roomSize = models.IntegerField(default=0)
	act = models.ForeignKey(Action, default=0, related_name='act_room')
	
class User(models.Model):
	nickName = models.CharField(max_length=20, default="")
	room = models.ForeignKey(Room, default=0, related_name='room_user')
	headImg = models.FileField(upload_to="./data/", default="")
	def __str__(self):
		return self.nickName

