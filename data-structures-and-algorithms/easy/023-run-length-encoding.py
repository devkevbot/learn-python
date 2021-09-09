"""
Return the run-length encoding of an input string. For example, if
"AAABB" is given, output "3A2B". If runs of 10 or more letters exist,
they should be split into groups of 9 and any left over letters.
"""

def runLengthEncoding(string):
	"""
	Time: O(n) where n is the length of the input string
	Space: O(n)
	"""

	current_run = 1
	output = []

	for idx in range(1, len(string)):
		current_char = string[idx]
		previous_char = string[idx - 1]

		if current_char != previous_char or current_run == 9:
			output.append(f"{current_run}{previous_char}")
			current_run = 0


		current_run += 1

	last_character = string[len(string) - 1]
	output.append(f"{current_run}{last_character}")

	return "".join(output)
