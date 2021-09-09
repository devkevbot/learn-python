"""
Return an array that is sorted in ascending order.
Implement insertion sort to sort the array.
"""

def insertionSort(array):
	"""
	Time: Best = O(n), Average = O(n^2), Worst = O(n^2)
	Space: O(1)
	"""
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			swap(j, j - 1, array)
			j -= 1

	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
