with open("City Plan.txt", 'r', newline = '') as file1:
	first_input = file1.readline()
	FileZero = file1.read()
	

inputList = first_input.split(' ')

print(FileZero)

simulation = int(inputList[0])
intersections = int(inputList[1])
streets = int(inputList[2])
cars = int(inputList[3])
bonus_points = int(inputList[4])

all_second_input = []

print(inputList)
print(type(simulation))

with open("City Plan1.txt", 'w') as file2:
	file2.write(FileZero)


with open("City Plan1.txt", 'r', newline = '') as file1:

	for i in range(streets):
		second_input = file1.readline()

		inputList2 = second_input.split(' ')

		all_second_input.append(inputList2)


print(all_second_input)



	




