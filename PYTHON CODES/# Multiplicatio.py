# Multiplication table

num = int(input("Enter a number between 1 and 12: "))

for i in range(num):
	multiplication = num * i
	print(f'{num} * {i} = {multiplication}')


