from django.contrib import admin
from .models import User, Action, Room

# Register your models here.
#class UserInline(admin.StackedInline):
class UserAdmin(admin.ModelAdmin):
	model = User
	extra = 4
	fields = ['nickName', 'room']

#class RoomInline(admin.StackedInline):
class RoomAdmin(admin.ModelAdmin):
	#inlines = [UserInline]
	model = Room 
	extra = 4
	fields = ['roomName', 'roomSize', 'act']
	
class ActionAdmin(admin.ModelAdmin):
	model = Action
	extra = 4
	fields = ['actName', 'actNum']
	#inlines = [RoomInline]
	
admin.site.register(Action, ActionAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)

