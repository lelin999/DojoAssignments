#find/replace - print position of "monkey" and then replace all "monkey" with alligator
string = "If monkeys like bananas, then I must be a monkey!"
pos = 0
while string.find("monkey", pos) != -1:
	loc = string.find("monkey", pos)
	print loc
	pos = loc + 5
print string.replace("monkey", "alligator")

#min/max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

#first/last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0] + x[len(x) - 1]
y = []
y.extend((x[0], x[len(x) - 1]))
print y

#new list
newArr = []
y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
for num in reversed(y):
	if num < 0:
		newArr.append(num)
		y.remove(num)
newArr.sort()
y.insert(0, newArr)
print y