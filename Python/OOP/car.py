class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()

	def display_all(self):
		print ("Price: ${}\nSpeed: {} mph\nFuel: {} mpg\nMileage: {} miles\nTax: {}").format(self.price, self.speed, self.fuel, self.mileage, self.tax)

mercedes = Car(40000, 150, 30, 250000)
honda = Car(20000, 100, 25, 200000)

# mercedes.display_all()
# honda.display_all()