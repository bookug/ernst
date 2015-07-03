#coding=utf-8

from django.db import models
from random import *

global empty_size
space_size = 80		#0 means empty

# Create your models here.
class Solution(models.Model):
	matrix = models.CharField(max_length=81, default='123456789456789123789123456234567891567891234891234567345678912678912345912345678')

	def __str__(self):
		return self.matrix
	def generate_question(self):
		global space_size
		num = randint(1, space_size)
		newmatrix = self.matrix			#string is not modifiable, so no copy(deep?) problem
		pos_list = []
		while num > 0:
			pos = randint(0, 80)
			if newmatrix[pos] == '0':
				continue
			else:
				newmatrix = newmatrix[0:pos] + "0" + newmatrix[pos+1:]
				num -= 1
				pos_list.append(pos)
		if not Question.objects.filter(matrix=newmatrix):
			question = Question(matrix=newmatrix)
			question.save()
			question.solutions.add(self)
			#compute the difficulty for this question: according to space freedom
			#S(i,j)=S(i)+S(j)+g(i,j) F=sum:S(i,j)  N:num of space (not include self)
			#range: all 0 -> 81*(8×2+4)=1620; one 0 -> 0; no 0 -> 0 
			#level: [0~540) 0; [540, 1080) 1; [1080, 1620) 2; 1620 is highest but so easy!(not used)
			#no space is also level 0, but not for playing, used as default
			space_freedom_sum = 0
			for pos in pos_list:
				x = pos // 9
				y = pos % 9
				grid_x = x // 3
				grid_y = y // 3
				for i in range(3):
					for j in range(3):
						ti = 3 * grid_x + i
						tj = 3 * grid_y + j
						if ti != x or tj != y:
							if newmatrix[ti*9+tj] == '0':
								space_freedom_sum += 1
				for i in range(9):
					if i //3 != grid_x and newmatrix[i*9+y] == '0':
						space_freedom_sum += 1
					if i //3 != grid_y and newmatrix[x*9+i] == '0':
						space_freedom_sum += 1
			question.rank = space_freedom_sum // 540
		else:
			question = Question.objects.get(matrix=newmatrix)
			if self not in question.solutions:
				question.solutions.add(self)
		question.save()
		return question

	def generate_solution(self):	
		#swap columns or rows in triple
		newmatrix = self.matrix
		pos1 = randint(0, 2)
		pos2 = randint(0, 2)
		while pos2 == pos1:
			pos2 = randint(0, 2)
		i = 0
		j = 0
		if randint(0, 1) == 0:
			while i < 3:
				while j < 9:
					p1 = pos1 * 27 + i * 9 + j
					p2 = pos2 * 27 + i * 9 + j
					print pos1, pos2, i, j
					t = newmatrix[p1]
					newmatrix = newmatrix[0:p1] + newmatrix[p2] + newmatrix[p1+1:]
					newmatrix = newmatrix[0:p2] + t + newmatrix[p2+1:]
					i += 1
					j += 1
		else:
			while j < 3:
				while i < 9:
					p1 = i * 9 + pos1 * 3 + j
					p2 = i * 9 + pos2 * 3 + j
					print pos1, pos2, i, j
					t = newmatrix[p1]
					newmatrix = newmatrix[0:p1] + newmatrix[p2] + newmatrix[p1+1:]
					newmatrix = newmatrix[0:p2] + t + newmatrix[p2+1]
					i += 1
					j += 1
		if not Solution.objects.filter(matrix=newmatrix):
			solution = Solution(matrix=newmatrix)
			solution.save()



class Question(models.Model):
	matrix = models.CharField(max_length=81, default='123456789456789123789123456234567891567891234891234567345678912678912345912345678')
	solutions = models.ManyToManyField(Solution, default=0)
	rank = models.IntegerField(default=0)

	def __str__(self):
		return self.matrix

	def get_solutions(self):
		return self.solutions.all()	

