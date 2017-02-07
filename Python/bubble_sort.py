def bubblesort(arr):
	for i in range(len(arr) - 1):
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
	for j in range(len(arr) - 1):
		if arr[j] > arr[j+1]:
			bubblesort(arr)
	return arr

x = [6,5,3,1,8,2,7]
print bubblesort(x)