# Problem 1 - Giving you the longest word in a set of text. 
def longestWord( text ):
	word = ''
	longest_word = ''
	max_length = 0

	for char in text: 
		if char.isalnum():
    			word += char
		elif word != '':
			if len(word) > max_length:
				max_length = len(word)
				longest_word = word
			word = ''

	#Handle last word (If string doesn't end in punctuation)
	if word != '':
		if len(word) > max_length:
			longest_word = word

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


#Problem 6 - Determine if the brackets in a string are balanced ({[]}) - balanced (({[}]) - Unbalanced
# My answer was wrong :[ - Le sad. I'll post corrected answer below.
#Wrong answer --
def is_balanced (s):
	bA = ("(", ")")
	bB = ("[", "]")
	bC = ("{", "}")
	check = true

	# Reverse the input string
	reverse = s[::-1]

	for i in range (len(s)):
		#If the forward and backward strings doesn't match A,B or C, they aren't balanced.
		if (s[i],reverse[i]) != bA || s[i],reverse[i]) != bB || s[i],reverse[i]) != bC)
			check = false
	
	return check
#Correct Answer --
def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_map.values():  # opening brackets
            stack.append(char)
        elif char in bracket_map:  # closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Problem 7 - Find the Missing number. Numbers are arranged from 0->n missing exactly one number. 
def find_missing(nums):
    max_num = len(nums)
    num_dict = {}

    # Add all possible values into a dictionary
    for i in range(max_num + 1):
        num_dict[i] = 0

    # Remove all numbers that exist in nums
    for num in nums:
        if num in num_dict:
            del num_dict[num]

    # Return the only remaining key
    return list(num_dict.keys())[0]

# Problem 8 - Create a basic password checker - Weak | Medium | Strong | Very Strong
# 1 point for each of the following:
# 8 Characters - 1 point
# Has Uppercase & Lowercase letters - 1 point
# Contains a digit - 1 point
# Contains a special character - 1 point
import re

def check_password( password ):
	points = 0
	results = ""

	#Check for 8 characters
	if (re.search(".{8}+", password) != None):
		points +=1

	#Check Uppercase / Lowercase letters
	if (re.search("[A-Z]", password) != None && re.search("[a-z]") != None):
		points += 1

	#Check if it contains a digit
	if (re.search("[0-9]", password) != None):
		points += 1

	#Check if it contains a special character
	if (re.search("\W", password) != None):
		points += 1

	if (points == 0) || (points == 1):
		results = "Weak"
	elif points == 2:
		results = "Medium"
	elif points == 3:
		results = "Strong"
	elif points == 4
		results = "Very Strong"

	return results
