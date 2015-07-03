from django.db import models
from random import *

global empty_size
empty_size = 6		#0 means empty

# Create your models here.
class Solution(models.Model):
	matrix = models.CharField(max_length=81, default='123456789456789123789123456234567891567891234891234567345678912678912345912345678')

	def __str__(self):
		return self.matrix
	def generate_question(self):
		global empty_size
		num = randint(empty_size/2, empty_size)
		newmatrix = self.matrix
		while num > 0:
			pos = randint(0, 80)
			if newmatrix[pos] == '0':
				continue
			else:
				newmatrix = newmatrix[0:pos] + "0" + newmatrix[pos+1:]
				num -= 1
		if not Question.objects.filter(matrix=newmatrix):
			question = Question(matrix=newmatrix)
			question.save()
			question.solutions.add(self)
		else:
			question = Question.objects.get(matrix=newmatrix)
			if self not in question.solutions:
				question.solutions.add(self)
		question.save()
		#TODO: compute the difficulty for this question
		return question

	def generate_solution(self):	
		#swap columns or rows
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
	matrix = models.CharField(max_length=81, default='000000000000000000000000000000000000000000000000000000000000000000000000000000000')
	solutions = models.ManyToManyField(Solution, default=0)
	rank = models.IntegerField(default=0)

	def __str__(self):
		return self.matrix

	def get_solutions(self):
		return self.solutions.all()	

