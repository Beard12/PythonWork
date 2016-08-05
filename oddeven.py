def count2000():
	for x in range(1,2001):
		if x % 2 == 0:
			print "Number is {}. This is an even number.".format(x)
		else:
			print "number is {}. This is an odd number.".format(x)

count2000()