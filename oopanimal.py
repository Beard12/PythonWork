class Animal(object):
  def __init__(self, name = "animal"):
    self.health=100
    self.name=name
  def walk(self):
    self.health-=1
    if self.health <= 0:
      print "This " + self.name + " is so dead. It walked too far." 
    return self
  def run(self):
    self.health-=5
    if self.health <= 0:
      print "This " + self.name + " is so dead. It walked too far."
    return self 
  def displayHealth(self):
    print "This " + self.name + " has " + str(self.health) + " health. "
    return self


animal1 = Animal()
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
  def __init__(self, name = "dog"):
    super(Dog, self).__init__()
    self.health=150
    self.name = name
  def pet(self):
    self.health +=5
    return self

dog1 = Dog()
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
  def __init__(self, name = "dragon"):
    super(Dragon, self).__init__()
    self.health=170
    self.name = name
  def fly(self):
    self.health -=10
    if self.health <= 0:
      print "This " + self.name + " is so dead. It flew too far."
    return self
  def displayHealth(self):
    print "This is a dragon!"
    super(Dragon, self).displayHealth()
    

dragon1 = Dragon()
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()

# animal1.pet().fly().displayHealth()  tried to run code did not work, came up with error saying that animal1 did not have the attribute of pet()