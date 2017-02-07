#odd/even
def odd_even(num1, num2):
	for num in range(num1, num2+1):
		if num % 2 == 1:
			print "Number is " + str(num) + ". This is an odd number."
		else:
			print "Number is " + str(num) + ". This is an even number."

odd_even(1, 10)

#multiply
def multiply(l, n):
	res = [elem * n for elem in l]
	return res

a = [2,4,10,16]
b = multiply(a, 5)

#hacker challenge
def layered_multiples(arr):
	for ind in range(len(arr)):
		temp = arr[ind]
		arr[ind] = []
		while temp > 0:
			arr[ind].append(1)
			temp = temp - 1
	return arr

print layered_multiples(multiply([2,4,6,8], 3))

# def layered_multiples(arr):
# 	new_arr = []
# 	for i in range(len(arr)):
# 		array2 = []
# 		for i in range(arr[i]):
# 			array2.append(1)
# 		new_arr.append(array2)
# 	return new_arr