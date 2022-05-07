with open("City Plan.txt", 'r', newline = '') as rf:
	first_input = rf.readline()
	FileZero = rf.read()
	

inputList = first_input.split(' ')

print(FileZero)

simulation = inputList[0]
intersections = inputList[1]
streets = inputList[2]
cars = inputList[3]
bonus_points = inputList[4]

print(simulation)



