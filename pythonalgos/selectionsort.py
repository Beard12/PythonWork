import random
def selectionSort(arr):
	for j in xrange(len(arr)):
		minu = arr[j]
		idx = j
		for x in xrange(j,len(arr)):
			if arr[x] < minu:
				minu= arr[x]
				idx = x
		arr[idx] = arr[j]
		arr[j]=minu

	

arr = []
for x in range(0,100):
	arr.append(random.randint(0,10000))
print arr 
selectionSort(arr)
print arr
	


