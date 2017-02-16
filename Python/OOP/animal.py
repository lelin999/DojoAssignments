class Animal(object):
	def __init__(self, name, hp=100):
		self.name = name
		self.hp = hp
	def walk(self):
		self.hp -= 1
	def run(self):	
		self.hp -= 5
	def displayHp(self):
		print "Animal hp = {}".format(self.hp)

class Doge(Animal):
	def __init__(self, name):
		super(Doge, self).__init__(name)
		self.hp = 150
	def pet(self):
		self.hp += 5

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.hp = 170
	def fly(self):
		self.hp -= 10
	def displayHp(self):
		print "This is a dragon!"
		super(Dragon, self).displayHp()

jonny = Dragon('jonny')
jonny.fly()
jonny.displayHp()
jonny.fly()
jonny.displayHp()

animal = Animal('animal')
animal.fly()
