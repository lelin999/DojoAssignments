import random
def randnum():
	return int(round(random.random()))

# def coin_toss(num):
# 	print "Starting the program..."
# 	def helper(headCount, tailCount):
# 		x = randnum()
# 		if x == 0:
# 			headCount += 1
# 			print "Attempt #" + str(headCount + tailCount) + ": Throwing a coin... It's a head! ... Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " tail(s) so far"
# 		elif x == 1:
# 			tailCount += 1
# 			print "Attempt #" + str(headCount + tailCount) + ": Throwing a coin... It's a tail! ... Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " tail(s) so far"
# 	while num > 0:
# 		helper(headCount, tailCount)
# 		num -= 1
# 	print "Ending the program, thank you!"

def coin_toss(num) :
	print "Starting the program..."
	attempt = 1
	headCount = 0
	tailCount = 0
	while attempt <= num:
		x = randnum()
		if x == 0:
			headCount += 1
			print "Attempt #" + str(headCount + tailCount) + ": Throwing a coin... It's a head! ... Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " tail(s) so far"
		elif x == 1:
			tailCount += 1
			print "Attempt #" + str(headCount + tailCount) + ": Throwing a coin... It's a tail! ... Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " tail(s) so far"
		attempt += 1
	print "Ending the program, thank you!"	
coin_toss(10)