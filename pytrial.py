import csv


class Supermarket:

	def __init__(self):
		pass



	def ViewCatalogue(self):

		with open("Sales.csv", 'r', newline = '') as sf:
			self.all_products = sf.read()
			print(self.all_products)

			#print(self.all_products)


	def AddItem(self):
		Id = int(input("Enter the product id: "))
		product = input("Enter product name: ")
		price = int(input("Enter the price: "))

		with open("Sales.csv", 'a', newline = '') as sf:
			newSale = (Id, product, price)
			writer = csv.writer(sf)
			writer.writerow(newSale)

	def NewClient(self):
		firstName = input("Enter first name: ")
		lastName = input("Enter last name: ")

		while True:
			productId = input("\n\nEnter the product id: ")
			numItem = int(input("Enter the number of items you want to buy: "))
			BreakChoice = input("\nDo you want to exit this tab?[yes/ no] ").lower()

			if BreakChoice == 'yes':
				break

			elif BreakChoice == 'no':
				continue
			else:
				print("Not a valid choice!!!!")
				BreakChoice = input("Do you want to exit this tab?[yes/ no] ").lower()
				if BreakChoice == 'yes':
					break

				elif BreakChoice == 'no':
					continue
				else:
					print("Not a valid choice!!!!")
					break

	def ViewSales(self):
		pass


s =  Supermarket()
while True:
	print("\n\n*****************SUPERMARKET SYSTEM*******************\n\n")
	print("Select an option\n")
	print("[1] View Catalogue\n")
	print("[2] Add item\n")
	print("[3] New Client\n")
	print("[4] View Sales\n")
	print("[5] Exit\n")

	choice = int(input("Your choice: "))


	if choice == 1:
		s.ViewCatalogue()

	if choice == 2:
		s.AddItem()

	if choice == 3:
		s.NewClient()

	if choice == 4:
		s.ViewSales()

	if choice == 5:
		exit()

