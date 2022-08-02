import heapq
from collections import deque

# Heap
lst = [5, 4, 3, 2, 1]
heapq.heapify(lst)
heapq.heappop(lst)  # 1
heapq.heappush(lst, 0)
heapq.heappop(lst)  # 0

# A deque (double-ended queue) is represented internally as a doubly linked list
# DLL Queue (FIFO)
queue = deque()
queue.append("Mary")
queue.append("John")
queue.popleft()  # Mary
# DLL Stack (LIFO)
stack = deque()
stack.appendleft("Mary")
stack.appendleft("John")
stack.popleft()  # John


# Singly linked list node
class SLLNode:
	def __init__(self, data):
		self.data = data
		self.next = None


# Double linked list node
class DLLNode:
	def __init__(self, value=None):
		self.value = value
		self.next = None
		self.prev = None


class DLL:
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def append(self, data):
		if self.head is None:
			self.head = DLLNode(data)
			self.tail = self.head
			self.count += 1
			return

		self.tail.next = DLLNode(data)
		self.tail.next.previous = self.tail
		self.tail = self.tail.next
		self.count += 1

	def insert(self, data, index):
		if (index > self.count) | (index < 0):
			raise ValueError(f"Index out of range: {index}, size: {self.count}")

		if index == self.count:
			self.append(data)
			return

		if index == 0:
			self.head.previous = DLLNode(data)
			self.head.previous.next = self.head
			self.head = self.head.previous
			self.count += 1
			return

		start = self.head
		for _ in range(index):
			start = start.next
		start.previous.next = DLLNode(data)
		start.previous.next.previous = start.previous
		start.previous.next.next = start
		start.previous = start.previous.next
		self.count += 1
		return

	def remove(self, index):
		if (index >= self.count) | (index < 0):
			raise ValueError(f"Index out of range: {index}, size: {self.count}")

		if index == 0:
			self.head = self.head.next
			self.head.previous = None
			self.count -= 1
			return

		if index == (self.count - 1):
			self.tail = self.tail.previous
			self.tail.next = None
			self.count -= 1
			return

		start = self.head
		for i in range(index):
			start = start.next
		start.previous.next, start.next.previous = start.next, start.previous
		self.count -= 1
		return

	def index(self, data):
		start = self.head
		for i in range(self.count):
			if start.data == data:
				return i
			start = start.next
		return
