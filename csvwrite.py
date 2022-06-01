import csv

file = open("csvwrite.csv", 'r')
search = input("Enter the data you are searching for: ") 
reader = csv.reader(file) 
for row in file:
	if search in str(row):
		print(row)