# Creates a file at the same folder this file is

with open("test1.txt.txt", 'r') as rf:
	with open("12345.txt", 'w') as wf:
		for line  in rf:
			wf.write(line)


