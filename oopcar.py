class Car(object):
	def __init__(self,price, speed,fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = .15
		else: 
			self.tax = .12
		self.displayAll()


	def displayAll(self):
		print "Price:", self.price
		print "Speed: " + str(self.speed) + "mph"
		print "Fuel:", self.fuel
		print "Mileage: " + str(self.mileage) + "mpg"
		print "Tax:", self.tax
		print "\n"


Car1 = Car(5000, 75, "Full", 20)
Car2 = Car(50000, 100, "Not Full", 10)
Car3 = Car(7000, 55, "Empty", 35)
Car4 = Car(800000, 200, "Full", 50)
Car5 = Car(500, 20, "Maybe", 9)

