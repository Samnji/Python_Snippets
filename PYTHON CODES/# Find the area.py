# Find the area of a square or a triangle

print("1) Square")
print("2) Triangle")

num1 = int(input("Enter a number:"))

if num1 == 1:
	length = int(input("Enter the length of the Square:"))

	area = length ** 2

	print("The area of the Square is", area)
elif num1 == 2:
	base = int(input("Enter the base of the Triangle:"))
	height = int(input("Enter the height of the Triangle:"))

	area = 1 / 2 * base * height

	print("The area of the Triangle is", area)
else:
	print("Invalid number")


