import random
import time
def bubblesort(arr):
	for i in range(len(arr)-1):
		for j in range((len(arr)-1)-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]= arr[j+1],arr[j]
						
arrb = []
for x in range(0,100):
	arrb.append(random.randint(1,10000))

 
stime = time.time()	
bubblesort(arrb)
etime = time.time()
print arrb
print (etime-stime)