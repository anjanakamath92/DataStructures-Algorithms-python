class Queue:

	def __init__(self):
		self.items = []
		self.size = 0

	def isEmpty(self):
		print "Empty Queue"
		return self.items == []

	def enqueue(self, item):
	#list.insert(index, obj) - inserts object obj into list at offset index
		self.items.insert(0, item)
		self.size += 1

	def dequeue(self):
		data = self.items.pop()
		self.size -= 1
		return data

	def printQueue(self):
		for item in self.items:
			print item, 

	def size(self):
		return len(self.items)


queue = Queue()
queue.isEmpty()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.printQueue()
print("\n")
queue.dequeue()
queue.printQueue()
