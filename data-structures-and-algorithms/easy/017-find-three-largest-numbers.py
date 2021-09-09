"""
Return the three largest numbers in an array in ascending order without sorting the input array given.
Duplicates may be returned.
"""

def findThreeLargestNumbers(array):
	"""
	Time: O(n) - loop through each element
	Space: O(1) - no new arrays allocated, no recursion
	"""
	big = None
	med = None
	small = None

	for number in array:
		if big is None or number > big:
			small = med
			med = big
			big = number
		elif med is None or number > med:
			small = med
			med = number
		elif small is None or number > small:
			small = number

	return [small, med, big]
