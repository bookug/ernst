from django.shortcuts import render
from .models import Question, Solution
from random import *

# Create your views here.
global active_question
active_question = Question()
global matrix
matrix=[None] * 3
for i1 in range(3):
	matrix[i1] = [None] * 3
	for j1 in range(3):
		matrix[i1][j1] = [None] * 3
		for i2 in range(3):
			matrix[i1][j1][i2] = [None] * 3
			for j2 in range(3):
				matrix[i1][j1][i2][j2] = '0'

#TODO: difficulty? compute space freedom!

def initialize(request):
	global matrix
	for question in Question.objects.all():
		question.delete()
	for solution in Solution.objects.all():
		solution.delete()
	Solution().save()
	return render(request, 'sudoku/init.html', {'message':"Initialization done!"})

def index(request):			#display a default sudoku problem	
	global matrix
	context = {'question':matrix}
	return render(request, 'sudoku/index.html', context)

def play(request):	#produce a question, maybe new
	global matrix
	global active_question
	level = request.POST.get('level') #TODO: select difficulty, maybe not exist
	solution = choice(Solution.objects.all())
	active_question = solution.generate_question()
	#solution.generate_solution()	#BETTER: add this 
	for i1 in range(3):	#len(matrix)
		for j1 in range(3):
			for i2 in range(3):
				for j2 in range(3):
					pos = i1 * 27 + i2 * 9 + j1 * 3 + j2
					c = active_question.matrix[pos]
					if c == '0':
						matrix[i1][j1][i2][j2] = "<input type='text' maxlength='1' name=" + str(pos) + " />"
					else:
						matrix[i1][j1][i2][j2] = "<input type='text' maxlength='1' value=" + c +" name=" + str(pos) + " disabled='disabled' />"
	#print matrix
	return render(request, 'sudoku/index.html', {'question':matrix})

def check(request):
	global matrix
	test = matrix
	flag = True
	temp = set([1,2,3,4,5,6,7,8,9])
	col = row = [[]] * 9
	for i1 in range(3):
		for j1 in range(3):
			grid = []
			for i2 in range(3):
				for j2 in range(3):
					pos = i1 * 27 + i2 * 9 + j1 * 3 + j2
					if test[i1][j1][i2][j2] == '0':
						test[i1][j1][i2][j2] = request.POST.get(str(pos))
					grid.append(test[i1][j1][i2][j2])		
					row[i1*3+i2].append(test[i1][j1][i2][j2])
					col[j1*3+j2].append(test[i1][j1][i2][j2])
			if set(grid) != temp:
				flag = False
				break
		if flag == False:
			break
	for k in range(9):
		if set(row[k]) != temp or set(col[k]) != temp:
			flag = False
			break
	if flag == True:
		reply = "Your answer is correct!"
	else:
		reply = "Your answer is wrong!"
	print reply
	print test
	context = {'message':reply, 'question':test}
	return render(request, 'sudoku/index.html', context)

def answer(request):
	global active_question
	#TODO:select solutions
	context = {'message':"this is the answer!", 'question':ans}
	return render(request, 'sudoku/index.html', context)

