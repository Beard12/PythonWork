def draw_stars(arr):
	for x in range(0, len(arr)):
		count = arr[x]
		if type(count) is str:
			print count[0].lower() * len(count),
			print ("\n")
		else:
			for i in range(0, count):
				print "*",
			print("\n")



x=[4,6,1,3,5,7,25]

b=[4, "Tom", 1, "Micheal", 5, 7, "Jimmy Smith"]
draw_stars(b)