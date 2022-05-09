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

	

