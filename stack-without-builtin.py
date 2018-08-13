class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:
	def __init__(self):
		self.head = None
		self.size = 0

	def push(self, item):
#		node = Node(item)
#		if self.head == None:
#			self.head = node
#		else:
#			node.next = self.head
#			self.head = node
#		self.size += 1
		temporaryNode = self.head
		self.head = item
		self.head.next = temporaryNode
		del temporaryNode
		self.size += 1 

	def pop(self):
		if self.size == 0:
			print "Stack is empty"
		item = self.head.value
		self.head = self.head.next
		del item


	def printStack(self):
		currentNode = self.head
		while True:
			if currentNode != None:
				print currentNode.value
				currentNode = currentNode.next
			else:
				break	
firstElement = Node(10)
stack = Stack()
stack.push(firstElement)
secondElement = Node(20)
stack.push(secondElement)
thirdElement = Node(30)
stack.push(thirdElement)
stack.printStack()
stack.pop()
stack.printStack()
