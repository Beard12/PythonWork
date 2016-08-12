class Bike(object):
	def __init__(self,miles =0):
		self.max_speed = 25
		self.price = 200
		self.miles = miles
	def displayInfo(self):
		print "This bike's max speed is {}mph! Wowzer and the price is only {} ".format(self.max_speed, self.price)
		print "What a steal especially when you consider, the bike has {} miles on it".format(self.miles)
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		if self.miles < 5:
			print "You can't reverse anymore man. Quit trying."
		else:
			self.miles -=5
		return self

bike1 = Bike()
bike2 = Bike()
bike3 = Bike()

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()

