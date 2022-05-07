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


