# DIctionary of favourite foods and asked which to remove then sort and display them

foods = {}

for i in range(4):
	food = input(f'Enter food {i + 1}: ')
	key = i + 1
	value = food

	foods[key] = value

print(foods)

remove_food = int(input("Enter the food index to remove: "))

del foods[remove_food]
#foods.pop(remove_food)

print(sorted(foods.values()))
