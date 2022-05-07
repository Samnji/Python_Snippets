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


