class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print self.price
		print self.max_speed
		print self.miles
	def riding(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		if (self.miles > 0):
			self.miles -= 5
		else:
			print "You can't go back anymore!"
		return self

bike1 = Bike("$25000", "60 mph")
fancybike = Bike("$500000", "150 mph", 10)
shittybike = Bike("$10", "1 mph", 10)

bike1.riding().riding().riding().reverse().displayInfo()
fancybike.riding().riding().reverse().reverse().displayInfo()
shittybike.reverse().reverse().reverse().displayInfo()