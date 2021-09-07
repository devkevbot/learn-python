"""
Given a sorted linked list, remove duplicate values and maintain the sorted order.
"""

# This is an input class. Do not edit.
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	"""
	Time: O(n)
	Space: O(1)
	"""
	current_node = linkedList

	while current_node is not None:
		next_node = current_node.next

		while next_node is not None and next_node.value == current_node.value:
			next_node = next_node.next

		current_node.next = next_node
		current_node = next_node

	return linkedList
