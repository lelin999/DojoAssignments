# #part I
x = [4,6,1,3,5,7,25]

def draw_stars(arr):
	for i in range(len(arr)):
		string = ""
		j = 0
		while j < arr[i]:
			string += "*"
			j += 1
		print string

draw_stars(x)

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
#part II
def draw_starsII(arr):
	for i in range(len(arr)):
		string = ""
		j = 0
		if type(arr[i]) is int:
			while j < arr[i]:
				string += "*"
				j += 1
			print string
		elif type(arr[i]) is str:
			while j < len(arr[i]):
				string += arr[i][0].lower()
				j+=1
			print string

draw_starsII(y)