#mutiples
#part 1
for num in range(1, 1000, 2):
	print num
#part 2
for num in range(5, 1000001, 5):
	print num

#sumlist
def sumList(list):
	total = 0
	for num in list:
		total += num
	print total
	return total

#averagelist
a = [1,2,5,10,255,3]
print sumList(a) / len(a)