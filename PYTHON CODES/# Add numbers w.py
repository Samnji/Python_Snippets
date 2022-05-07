# Add numbers which are entered five times and given permision

total = 0

for i in range(2):
	num = int(input("Enter a number: "))
	quiz = input("Do you want this number to be added?[yes, no] ")

	if quiz == 'yes':
		total = total + num

print(f'The total is {total}')


