# Message encreption decreption system using random secret key
import random
def Encode(msg, num):
	m = msg
	n= num
	encodedMsg = ''

	for letter in msg:
		letterIndex = alphabets.index(letter)
		encodedLetterIndex = letterIndex + num
		if encodedLetterIndex > 26:
			encodedLetterIndex -= 27
		encodedLetter = alphabets[encodedLetterIndex]

		encodedMsg += encodedLetter


	print(encodedMsg)


def Decode(msg, num):
	m = msg
	n= num
	encodedMsg = ''

	for letter in msg:
		letterIndex = alphabets.index(letter)
		encodedLetterIndex = letterIndex - num
		if encodedLetterIndex < 0:
			encodedLetterIndex += 27
		encodedLetter = alphabets[encodedLetterIndex]

		encodedMsg += encodedLetter


	print(encodedMsg)


alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


while True:
	print("\n************Welcome to Encreption and Decreption System****************\n\n")
	print("1) Make a code")
	print("2) Decode a message")
	print("3) Quit\n")
	choice = int(input("Enter your selection: "))


	if choice == 1:
		msg = input("Enter a message: ").lower()
		num = random.randrange(0, 15)

		Encode(msg, num)


	elif choice == 2:
		msg = input("Enter a message: ").lower()
		num = random.randrange(0, 15)



		Decode(msg, num)

	elif choice == 3:
		exit()
	else:
		print()