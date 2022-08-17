class Vehicle:
	def __init__(self, name, mileage, capacity):
		self.name = name
		self.mileage = mileage
		self.capacity = capacity

	def fare(self):
		return self.capacity * 100

class Bus(Vehicle):
	def fare(self):
		amount = super().fare()
		amount += amount * 10/100

		return amount
	

school_bus = Bus("School Volvo", 12, 50)

print(school_bus.fare())
print(type(school_bus))
print(isinstance(school_bus, Vehicle))
