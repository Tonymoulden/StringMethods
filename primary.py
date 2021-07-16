# author:
# date:

# --------------- Section 1 --------------- #

# 1 | String Methods
#
# 1 - Save your name to a variable named name.
#   a. Center that variable within 30 characters. Print it.
#   b. Print the variable in all upper case.
#   c. Print the variable in all lower case.
#   d. Print the variable capitalized (Look to documentation.)

print('Tony Moulden'.center(30, '~'))
Text = 'tony moulden'
print(Text.lower())
print(Text.upper())

# 2 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first instance of the letter a. Print that position.
#   b. Find the first instance of the letter b. Print that position.
#   c. Find the first instance of a word of your choice. Print that position.

text = input('Enter a Sentence Here!: ')
print(text)

print('position of the first a:', text.find('a'))
print('position of the first e:', text.find('a'))
print('position of Beyonce:', text.find('Beyonce'))

# 3 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the position of every vowel in text. Save them each to a variable.
#   b. Using a built-in function, print the position of the vowel that shows up last.
#   c. Using a built-in function, print the position of the vowel that shows up first.

text = input('Enter a Sentence Here!: ')
print(text)

vowel1 = ('position of the first a:', text.find('a'))
vowel2 = ('position of the first e:', text.find('e'))
vowel3 = ('position of the first i:', text.find('i'))
vowel4 = ('position of the first o:', text.find('o'))
vowel5 = ('position of the first u:', text.find('u'))

print('the position of a is: ', vowel1)
print('the position of e is: ', vowel2)
print('the position of i is: ', vowel3)
print('the position of o is: ', vowel4)
print('the position of u is: ', vowel5)
# 4 | String Indexing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the 0th letter of the text using string indexing.
#   b. Print the 1st, 2nd, and 3rd letters of the text using string indexing.
#   c. Print the last letter of the text using string indexing.
#       HINT: There are multiple ways of doing this. Is there a function that we can use that will find
#           the position of the last letter, or atleast one off from it?

text = input('Enter a Sentence Here!: ')
print(text)

print(text[0])
print(text[1], text[2], text[3])
print(text[-1])

# 5 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Slice text from the 2nd position to the 5th. Print that.
#   b. Slice text from the 0th position to the 8th. Print that.
#   c. Slice text from 3rd position to end. Print that.
#   d. Slice text from the beginning to 5 positions before the last character. Print that.
#       HINT: Use a function to get the last position of the string.

text = input('Enter a Sentence Here!: ')
print(text[2:5])
print(text[0:8])
print(text[3:])
print(text[:])

# 6 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the text, but only every 2nd character.
#   b. Print the text, but only every 3rd character.
#   c. Print the text, but in reverse order.

text = input('Enter a Sentence Here!: ')
print(text[::2])
print(text[::3])
print(text[::-1])

