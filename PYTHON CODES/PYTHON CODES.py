#String slicing

song = input("Enter the first line of a nursery rhyme: ")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(song[start:end])


#String with ifelse statement

fname = input("Enter your first name: ")

if len(fname) < 5:
	surname = input("Enter your surname: ")
	full_name = fname + surname
	print(str.upper(full_name))
elif len(fname) >= 5:
	print(str.lower(fname))

#String with ifelse statement(pig latin addtion of string to the end)

word = input("Enter a word: ")
length = len(word)
first = word[0]
rest_word = word[1:length]
if word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
	final_word = rest_word + word[0] + 'ay'
else:
	final_word = word + 'way'
print(final_word.lower())


# Draw boxes filled with different colors

import turtle

turtle.color("black", "red")
turtle.begin_fill()

for i in range(4):
	turtle.forward(70)
	turtle.delay(10)
	turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()

for i in range(4):
	turtle.forward(70)
	turtle.delay(10)
	turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()

for i in range(4):
	turtle.forward(70)
	turtle.delay(10)
	turtle.right(90)

turtle.end_fill()

turtle.exitonclick()


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


# Display your name for the number of times you enter

name = input("Enter your name: ")
num = int(input("Enter a number: "))

for i in range(num):
	for i in name:
		print(i)


# Multiplication table

num = int(input("Enter a number between 1 and 12: "))

for i in range(num):
	multiplication = num * i
	print(f'{num} * {i} = {multiplication}')


# Print numbers from 50 to the specificied number

num = int(input("Enter a number less than 50: "))

for i in range(50, num -1 , -1):
	print(i)


# Print a name the number of times entered if less than 10

name = input("Enter your name:")
num = int(input("Enter a number: "))

if num < 10:
	for i in range(num):
		print(name)
else:
	for i in range(3):
		print("Too High!!!")



# Add numbers which are entered five times and given permision

total = 0

for i in range(2):
	num = int(input("Enter a number: "))
	quiz = input("Do you want this number to be added?[yes, no] ")

	if quiz == 'yes':
		total = total + num

print(f'The total is {total}')


#Students marks averaging showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    list_of_marks = student_marks[query_name]

    marks = 0

    for mark in list_of_marks:
        marks = marks + mark


    avg = marks / len(list_of_marks)
    
    print("%.2f" % avg)
    


#Phonebook entry and searching

n = int(input())
phoneBook = dict()

for i in range(n):
    words = input().split(' ')
    key = words[0]
    value = words[1]
    phoneBook[key]=value

print(phoneBook)

for i in range(n):
    name = input()
    if name in phoneBook:
        print(f'{name}={phoneBook[name]}')
    else:
        print("Not found")


#The pizza shop like and dislikes

n = int(input())
likes = []
dislikes = []

for i in range(n):
    like = input().split(' ')
    like.pop(0)
    
    for l  in like:
        if l not in likes:
            likes.append(l)

    dislike = input().split(' ')
    dislike.pop(0)
    
    for dl  in dislike:
        if dl not in dislikes:
            dislikes.append(dl)
    
    
totsLike = []

for name in likes:
    if name not in dislikes:
        totsLike.append(name)
        
str_totsLike = ' '.join(totsLike)
print(f'{len(totsLike)} {str_totsLike}')



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



# Creates a file at the same folder this file is

with open("test1.txt.txt", 'r') as rf:
	with open("12345.txt", 'w') as wf:
		for line  in rf:
			wf.write(line)


# Student Note Uploading System

class School:
	def __init__(self):
		self.students = dict()
		self.all_notes = dict()

	def AddStudent(self):
		self.student = dict()

		firstName = input("Enter student's first name: ")
		lastName = input("Enter student's last name: ")
		number =int(input("Enter student's pohone number: "))
		regNo = input("Enter student's registration number: ")
 
		details = [firstName, lastName, number]

		self.student[regNo]= details

		self.students.update(self.student)

	def SearchStudent(self):
		regNo = input("Enter regNo:")

		if regNo in self.students:
			details = self.students[regNo]

			print(details[0], details[1])

		else:
			print("Student not found!!!!")



	def AddFile(self):
		regNo = input("Enter regNo:")

		if regNo in self.students:
			self.note = dict()

			subject = input("Enter subject: ")
			self.fileName = input("Enter file Name: ")
			
			
	 
			noteDetails = [subject, self.fileName]

			self.note[regNo]= noteDetails

			self.all_notes.update(self.note)

			try:
				with open(self.fileName, 'r') as self.rf:
					with open(f'{self.fileName}_copy.txt', 'w') as self.wf:
						for line in self.rf:
							self.wf.write(line)
			except:
				print("File name not in the folder!!!!")


		else:
			print("You can't add notes because you are not in the system!!!!")


	def SearchFile(self):
		regNo = input("Enter regNo:")

		if regNo in self.students:
			searchFileName = input("Enter file name:")

			searchNoteDetails = self.all_notes[regNo]

			if searchFileName in searchNoteDetails:

				print(searchNoteDetails[0], searchNoteDetails[1])


			else:
				print("File not found!!!!")


		else:
			print("Student not found!!!!")


	def PrintFileReport(self):
		regNo = input("Enter regNo:")

		if regNo in self.students:

			searchNoteDetails = self.all_notes[regNo]
			details = self.students[regNo]

			print()

			print(f'''{details[0]} {details[1]}\'s report contains the following:\nHis phone number is {details[2]} and has submittted the following file {searchNoteDetails[1]} based on {searchNoteDetails[0]}.\nThe file contains the following:''')

			with open(f'{self.fileName}_copy.txt', 'r') as your_copyFile:
				print(your_copyFile.read())


		else:
			print("Student not found!!!!")



		
s = School()

while True:
	

	print("\n------------School Control---------------\n\n")
	print("Choose a number to execute an option\n")
	print("[1] Add student")
	print("[2] Search student")
	print("[3] Add notes")
	print("[4] Search file")
	print("[5] Print file report")
	print("[6] Exit")
	choose = int(input("Your choose: "))

	
	if choose == 1:
		
		s.AddStudent()

	elif choose == 2:
		s.SearchStudent()

	elif choose == 3:
		s.AddFile()

	elif choose == 4:
		s.SearchFile()

	elif choose == 5:
		s.PrintFileReport()

	elif choose == 6:
		exit()

	






