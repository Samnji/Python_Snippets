# phoneBook application

class phoneBook:

	def __init__(self):
		self.All_contacts = dict()

	def NewContact(self):
		self.ContactList = dict()

		key = input("Enter name:")
		value = int(input("Enter number:"))

		self.ContactList[key]= value

		self.All_contacts.update(self.ContactList)

	def SearchByName(self, ):
		self.name = input("Enter name:")

		num = self.All_contacts[self.name]
		print(f'{self.name} {num}')

p = phoneBook()


while True:
	print("\n------------My Agender---------------\n\n")
	print("Choose a number to execute an option\n")
	print("[1] New Contact")
	print("[2] Search by Name")
	print("[3] Exit")
	choose = int(input("Your choose: "))

	
	if choose == 1:
		p.NewContact()
		
		
	elif choose == 2:
		numSearch = p.SearchByName()
		

	elif choose == 3:
		exit()



