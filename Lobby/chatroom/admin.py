from django.contrib import admin
from .models import Room, Message

# Register your models here.

#class MessageInline(admin.StackedInline):
class MessageAdmin(admin.ModelAdmin):
	model = Message
	extra = 4
	#fields=[]

class RoomAdmin(admin.ModelAdmin):
	#inlines = [MessageInline]
	model = Room
	extra = 4
	#fileds=[]

admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)

