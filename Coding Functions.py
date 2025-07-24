# Problem 1 - Giving you the longest word in a set of text. 
define longestWord( text ):
	word = ''
	longest_word = ''
	max_length = 0

	for char in text: 
		if char.isalnum():
    			word += char
		elif word != ''
			if len(word) > max_length:
				max_length = len(word)
				longest_word = word
			word = ''

	return longest_word

# Problem 2 - Adding two numbers tog
def two_sum ( number_list , target )
	for number in number_list:
		if ( number_list - target in number_list ):
			return (number, target - number)

	return None

#Problem 3 - Removing Duplicates from a list of items
def remove_duplicates( list )
	seen = []
	for item in list:
		if item not in seen:
			seen.append(item)
	
	return seen

#Problem 4 - Giving you the most frequent item in a list
def most_frequent( inList ):
	counter_dictionary = {}
	counter_max = 0
	counter_maxKey = ""
	for item in inList:
		if item not in counter_dictionary:
			counter_dictionary[item] = 1
		else: 	
			counter_dictionary[item] += 1
		
		if counter_dictionary[item] > counter_max:
			counter_maxKey = item
		
	return counter_maxKey

# Problem 5 - Compressing text such that the order of text that appears is displayed as a letter followed by a digit aaaabbcccaaa -> a4b2c3a3
def compress ( text )
	current_letter = ''
	current_count = 0
	output_string = ""

	for i in range(len(text)):
		if current_letter != text[i]:
			# First iteration
			if i!= 0:
				output_string += current_letter + str(current_count)
			current_letter = text[i]
			current_count = 1

		elif current_letter == text[i]:
			current_count +=1
			
		
		#Final iteration - Make sure it's added to the output string
		if i == len(text)-1:
			output_string += current_letter + str(current_count)


	return output_string
