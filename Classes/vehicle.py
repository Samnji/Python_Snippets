class  Vehicle:
	color = "white"
	def __init__(self, name, max_speed, mileage, capacity):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage
		self.capacity = capacity

	def seatingCapacity(self):
		return f"The seating capacity of {self.name} is {capacity} passengers."

	def fare(self):
		return capacity * 100
		print(f"The total fare for {self.name} is {capacity * 100}")

class Bus(Vehicle):
	def seatingCapacity(self, capacity = 50):
		return f"The seating capacity of {self.name} is {capacity} passengers."

	def fare(self):
		final_amount= super().fare()
		final_amount += 0.1 * final_amount
		print(f"The total fare for {self.name} is {final_amount}")

class Car(Vehicle):
	color = "red"
	def seatingCapacity(self, capacity = 5):
		return f"The seating capacity of {self.name} is {capacity} passengers."


school_bus = Bus("School Volvo", 180, 12, 40)
vitz = Car("Vitz", 150, 15, 30)

school_bus.fare()
vitz.fare()
