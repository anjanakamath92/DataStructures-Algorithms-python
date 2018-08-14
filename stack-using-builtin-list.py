class Stack:
	def __init__(self):
		self.items = []
		self.size = 0

	def isEmpty(self):
		print "Empty Stack"
		return self.items == []
	
	def push(self, item):
		# adds a single element to the end of list 
		self.items.append(item)
		self.size += 1 

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def printStack(self):
		for item in self.items:
			print item,


stack = Stack()
stack.isEmpty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.printStack()
print "\n"
stack.pop()
stack.printStack()


