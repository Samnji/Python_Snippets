import re

with open("PYTHON CODES.py", 'r') as rf:
	FileZero = rf.read()

char = "#"
indices = [i.start() for i in re.finditer(char, FileZero)]
print(indices)

j = 0
for item in indices:
  print(F'This is where it breaks {FileZero[j:item]}')

  j = item
