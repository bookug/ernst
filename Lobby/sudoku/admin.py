from django.contrib import admin
from .models import Solution, Question 

# Register your models here.
class SolutionAdmin(admin.ModelAdmin):
	model = Solution
	extra = 4
	fields = ['matrix']

class QuestionAdmin(admin.ModelAdmin):
	model = Question
	extra = 4
	fields = ['matrix', 'solutions']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Solution, SolutionAdmin)

