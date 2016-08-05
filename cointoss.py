import random
def cointoss():
	toss=random.random()
	check = round(toss)
	return check
count = 1
tail=0
head=0
while count <= 5000:
	string =""
	toss=cointoss()
	if toss == 1:
		head += 1
		string = "head"
	else:
		tail+= 1
		string = "tail"	
	print "Attempt #{}: Throwing a coin... It's a {}! .. Got {} head(s) so far and {} tail(s) so far".format(count,string,head,tail)
	count+=1