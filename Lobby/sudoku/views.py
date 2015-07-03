from django.shortcuts import render
from .models import Question, Solution
from random import *
from copy import *				#copy and deepcopy

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
global html_matrix
html_matrix = deepcopy(matrix)		#not use = directly

def initialize(request):
	for question in Question.objects.all():
		question.delete()
	for solution in Solution.objects.all():
		solution.delete()
	Solution().save()
	return render(request, 'sudoku/init.html', {'message':"Initialization done!"})

def index(request):			#display a default sudoku problem	
	global html_matrix
	for i in range(100):
		try:
			solution = choice(Solution.objects.all())
		except Exception,e:
			solution = Solution()
			solution.save()
		solution.generate_solution()	
		solution.generate_question()
	context = {'question':html_matrix}
	return render(request, 'sudoku/index.html', context)

def play(request):	#produce a question, maybe new
	global matrix
	global html_matrix
	global active_question
	level = int(request.POST.get('level'))
	try:
		active_question = choice(Question.objects.filter(rank=level))
	except Exception,e:
		active_question = None
		#print e
	if not active_question:
		while True:
			solution = choice(Solution.objects.all())
			solution.generate_solution()	
			active_question = solution.generate_question()
			if active_question.rank == level:
				break
	for i1 in range(3):	#len(matrix)
		for j1 in range(3):
			for i2 in range(3):
				for j2 in range(3):
					pos = i1 * 27 + i2 * 9 + j1 * 3 + j2
					c = active_question.matrix[pos]
					#BETTER: use select instead of input
					matrix[i1][j1][i2][j2] = c
					if c == '0':
						html_matrix[i1][j1][i2][j2] = "<input type='text' maxlength='1' name=" + str(pos) + " />"
					else:
						html_matrix[i1][j1][i2][j2] = "<input type='text' maxlength='1' value=" + c +" name=" + str(pos) + " disabled='disabled' />"
	return render(request, 'sudoku/index.html', {'question':html_matrix})

def check(request):
	global matrix
	test = deepcopy(matrix)
	flag = True
	temp = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
	col = row = [[None] * 9] * 9
	for i1 in range(3):
		for j1 in range(3):
			grid = []
			for i2 in range(3):
				for j2 in range(3):
					pos = i1 * 27 + i2 * 9 + j1 * 3 + j2
					if test[i1][j1][i2][j2] == '0':
						#print str(pos)
						test[i1][j1][i2][j2] = request.POST.get(str(pos))
						#print "assignment successfully!", test[i1][j1][i2][j2]
					grid.append(test[i1][j1][i2][j2])		
					row[i1*3+i2][j1*3+j2] = test[i1][j1][i2][j2]
					col[j1*3+j2][i1*3+i2] = test[i1][j1][i2][j2]
			if set(grid) != temp:
				flag = False
				break
		if flag == False:
			break
	for k in range(9):
		#print row[k], col[k]
		if set(row[k]) != temp or set(col[k]) != temp:
			flag = False
			break
	if flag == True:
		reply = "Your answer is correct!"
	else:
		reply = "Your answer is wrong!"
	context = {'message':reply, 'question':test}
	return render(request, 'sudoku/index.html', context)

def answer(request):
	global active_question
	sol = choice(active_question.get_solutions())
	ans=[None] * 3
	for i1 in range(3):
		ans[i1] = [None] * 3
		for j1 in range(3):
			ans[i1][j1] = [None] * 3
			for i2 in range(3):
				ans[i1][j1][i2] = [None] * 3
				for j2 in range(3):
					ans[i1][j1][i2][j2] = sol.matrix[i1*27+i2*9+j1*3+j2]
	context = {'message':"this is the answer!", 'question':ans}
	return render(request, 'sudoku/index.html', context)

