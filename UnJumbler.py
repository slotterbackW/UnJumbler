words = open("words.txt")

# Returns True if 'input' has the same letters as 'word'
def hasSameLetters(input, word):
	inp_len = len(input)
	if(len(word) is not inp_len):
		return False

	input_as_list = list(input)
	word_as_list = list(word)

	for letter in input_as_list:
		if letter not in word_as_list:
			return False
		else:
			word_as_list.remove(letter)
	return True

# Returns a list of all the possible words which can be made
# using the letters of the given words.
def unscramble(input):
	results = []
	for line in words:
		word = line.strip()
		if hasSameLetters(input, word):
			results.append(word)
	return results

# Returns true if the given word can be made out of the given letters
def wordCanBeMadeOutOfLetters(letters, word):
	list_letters = list(letters)
	list_word = list(word)

	for letter in list_word:
		if letter not in list_letters:
			return False
		else:
			list_letters.remove(letter)
	return True

# Returns a list of all the words of the given word_size which can be made
# out of the given letters
def find_words(letters, word_len):
	results = []
	for line in words:
		word = line.strip()
		if len(word) is word_len:
			if wordCanBeMadeOutOfLetters(letters, word):
				results.append(word)
	return results


def main():
	final_unscrambled_words = []

	# Unscramble 4 words
	count = 4
	while count > 0:
		words.seek(0)	
		print("\nEnter scrambled word:")
		word = input()
		unscrambled_words = unscramble(word)
		print('Possible unscrambled words: ' + ', '.join(unscrambled_words))

		if len(unscrambled_words) is 0:
			print('Oops! No unscrambled words found! Please try again')
		elif len(unscrambled_words) > 1:
			print('Multiple possible unscrambled words found. Please select which one to use,' +
			 ' by entering the position of the word you want to select (Zero-based): ')
			pos = int(input())
			selected_word = unscrambled_words[pos]
			final_unscrambled_words.append(selected_word)
			count -= 1
		else:
			final_unscrambled_words.append(unscrambled_words[0])
			count -= 1

	print('\nFinal list of unscrambled words: ' + ', '.join(final_unscrambled_words))

	print('\nNow to find the solution!\n')
	while True:
		print('Enter the letters to be used in the final word solution or \'Exit\' to end the program')
		letters = input()
		if letters.lower() == 'exit':
			break
		words.seek(0)
		print('Now enter the length of the word to find.')
		word_size = int(input())
		possible_words = find_words(letters, word_size)
		print('Possible words: ' + ', '.join(possible_words))
		print('\nNow for the next word.')

	words.close()

main()