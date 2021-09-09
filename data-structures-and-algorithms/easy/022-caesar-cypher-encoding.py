"""
Given a non-empty string of lowercase letters and a non-negative integer
representing a key, write a function that returns a new string obtained
by shifting every letter in the input string by k positions in the
alphabet, where k is the key.
"""

def caesarCipherEncryptor(string, key):
	"""
	Time: O(n) - loop through the string
	Space: O(n) - store each encrypted character
	"""
	encrypted_characters = []

	for character in string:
		encrypted_characters.append(shiftCharacter(character, key))

	return "".join(encrypted_characters)

def shiftCharacter(character, key):
	letter_a_ascii_value = 97
	letters_in_alphabet = 26
	character_ascii_value = ord(character)
	shifted_ascii_value = (character_ascii_value + key - letter_a_ascii_value)
	wrapped_ascii_value = shifted_ascii_value % letters_in_alphabet + letter_a_ascii_value
	return chr(wrapped_ascii_value)



