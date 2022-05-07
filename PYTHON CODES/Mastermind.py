import random

def Play():
	color = ["pink", "blue", "yellow", "red", "green", "white", "black", "brown"]
	comp_colors = []
	for i in range(4):
		comp_color= random.choice(color)
		comp_colors.append(comp_color)
	print(comp_colors)


while True:
	print("\n**********Mastermind Board Game**********\n\n")
	print("1} Play\n")
	print("2} Exit\n")

	choice = int(input("Enter your selection: "))

	if choice == 1:
		Play()
	elif choice == 2:
		exit()
	else:
		print("Enter a valid choice!!!!")