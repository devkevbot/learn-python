"""
Return an array that is sorted in ascending order.
Implement selection sort to sort the array.
"""

def selectionSort(array):
	"""
	Time: Best, Worst, Average all O(n^2)
	Space: O(1)
	"""

	sorted_idx = 0

	while sorted_idx != len(array):
		smallest_number_idx = sorted_idx

		for idx in range(sorted_idx + 1, len(array)):
			if array[idx] < array[smallest_number_idx]:
				smallest_number_idx = idx

		swap(sorted_idx, smallest_number_idx, array)
		sorted_idx += 1

	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]