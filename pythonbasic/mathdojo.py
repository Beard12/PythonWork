class MathDojo(object):
	def __init__(self, value = 0):
		self.value  = value 
	def add(self, *rest):
		for x in range(len(rest)):
			if type(rest[x]) is list:
				for j in range(len(rest[x])):
					self.value +=rest[x][j]
			if type(rest[x]) is tuple:
				for k in range(len(rest[x])):
					self.value += rest[x][k]
			if type(rest[x]) is int:
				self.value += rest[x]
		return self
	def subtract(self, *rest):
		for x in range(len(rest)):
			if type(rest[x]) is list:
				for j in range(len(rest[x])):
					self.value -=rest[x][j]
			if type(rest[x]) is tuple:
				for k in range(len(rest[x])):
					self.value -= rest[x][k]
			if type(rest[x]) is int:
				self.value -= rest[x]


		
		return self



md = MathDojo()

md.add(3,[4,5],(3,5)).subtract(2,4,[7,3],(3,4))

print md.value