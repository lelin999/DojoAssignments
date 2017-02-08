def selectionsort(arr):
	j = 0
	for i in range(j, len(arr)):
		if arr[i] > arr[i + 1]:
			indMin = arr.index(min(arr))
			arr[i], arr[indMin] = arr[indMin], arr[i]
			j += 1
	return arr

x = [6,3,1,5,7,0]
print selectionsort(x)