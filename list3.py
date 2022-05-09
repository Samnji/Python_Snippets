# Add people to invite in a party
names = []

for i in range(3):
	name = input("Enter a person you want to invite to the party: ")
	
	names.append(name)

ans1 = input("Do you want to add another name? [yes, no]: ").lower()

if ans1 == 'yes':
	while True:
		name = input("Enter a person you want to invite to the party: ")

		names.append(name)

		ans2 = input("Do you want to add another name? [yes, no]: ").lower()

		if ans2 == 'yes':
			continue
		elif ans2 == 'no':
			break
		else:
			print("Invalid Choice")


elif ans1 == 'no':
	exit()

else:
	print("Invalid Choice")

print(names)
