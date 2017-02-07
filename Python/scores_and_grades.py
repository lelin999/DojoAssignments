import random
def randnum():
	random_num = int(round((random.random() * 40 + 60), 0))
	return random_num

def scores_and_grades(n):
	print "Scores and Grades"
	def helper():
		x = randnum()
		if x > 89:
			print "Score:" + str(x) + "; Your Grade is A"
		elif x > 79:
			print "Score:" + str(x) + "; Your Grade is B"
		elif x > 69:
			print "Score:" + str(x) + "; Your Grade is C"
		elif x > 59:
			print "Score:" + str(x) + "; Your Grade is D"
	while n > 0:
		helper()
		n = n - 1
	print "End of the Program. Bye!"

scores_and_grades(10)