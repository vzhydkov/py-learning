import bisect
import heapq
from collections import deque


# Singly linked list node
class SLLNode:
	def __init__(self, data):
		self.data = data
		self.next = None


# Double linked list node
class DLLNode:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None


if __name__ == "__main__":
	# Heap (tree)
	lst = [5, 4, 3, 2, 1]
	heapq.heapify(lst)
	assert heapq.heappop(lst) == 1
	heapq.heappush(lst, 0)
	assert heapq.heappop(lst) == 0
	# last 3 largest in list
	assert heapq.nlargest(3, lst) == [5, 4, 3]

	# A deque (double-ended queue) is represented internally as a doubly linked list
	# DLL Queue (FIFO)
	queue = deque()
	queue.append("Mary")
	queue.append("John")
	assert queue.popleft() == "Mary"
	# DLL Stack (LIFO)
	stack = deque()
	stack.appendleft("Mary")
	stack.appendleft("John")
	assert stack.popleft() == "John"

	# Bisect (a, x[, lo[, hi]])
	lst = [33, 36, 40, 43, 44, 48, 50]
	assert bisect.bisect(lst, 42) == 3
	lst.insert(3, 42)
	# Suppose that the element you want to insert is already present in the list,
	# bisect_left() returns the index before that element
	assert bisect.bisect_left(lst, 42) == 3
	# bisect_right returns the index after that element
	assert bisect.bisect_right(lst, 42) == 4
	# used to insert the element in the list without disturbing the order of the list
	bisect.insort(lst, 41)
	assert lst == [33, 36, 40, 41, 42, 43, 44, 48, 50]
