import re

with open("PYTHON CODES.py", 'r') as rf:
	FileZero = rf.read()

char = "#"
indices = [i.start() for i in re.finditer(char, FileZero)]
print(indices)



#print(FileZero[0:196])

for item in indices:
	b = indices.index(item) 
	a = b - 1
	start = indices[a]
	end = indices[b]
	print(start, end)
	fileName = FileZero[start:start + 15]
	with open(f'{fileName}.py', 'w') as nf:
		string = FileZero[start : end]
		print(string)
		nf.write(string)

