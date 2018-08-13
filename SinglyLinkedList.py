# Create Nodes
# Create Linked List
# Add nodes to Linked list
# Print Linked List

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insertHead(self, newNode):
		# data => Matthew, next => None
		temporaryNode = self.head # John	
		self.head = newNode
		self.head.next = temporaryNode
		del temporaryNode

	def insertEnd(self, newNode):
		# head => John->None
		if self.head == None:
			self.head = newNode
		else:
			# head =>  John -> Ben -> None || John -> Matthew
			# self.head.next = newNode - no ideal

			#iterate over the entire list
			lastNode = self.head
			while True:
				if lastNode.next == None:
					break
				else:
					lastNode = lastNode.next
				
			lastNode.next = newNode

	def listLength(self):
		currentNode = self.head
		length = 0
		while currentNode != None:
			length += 1
			currentNode = currentNode.next
		return length

	def insertAt(self, newNode, position):
		if position < 0 or position > self.listLength():
			print "Invalid position"
			return		
		if position == 0:
			self.insertHead(newNode)
			return
		#Traverse the list
		currentNode = self.head
		currentPosition = 0
		while True:
			if  currentPosition == position:
				previousNode.next = newNode
				newNode.next = currentNode
				break
			previousNode = currentNode
			currentNode = currentNode.next
			currentPosition += 1

	def printList(self):
		# head => John->Ben->Matthew->None
		if self.head == None:
			print "List is empty"
			return

		currentNode = self.head
		while True:
			if currentNode == None:
				break
			else:
				print currentNode.data
				currentNode = currentNode.next

	def deleteEnd(self):
		#Traverse the list and delete the last node
		lastNode = self.head
		while lastNode.next != None:
			previousNode = lastNode
			lastNode = lastNode.next
		previousNode.next = None
		
	def deleteAt(self, position):
		if position < 0 or position >= self.listLength():
			print "Invalid position"
			return
		if self.isListEmpty() == False:
			if position == 0:
				self.deleteHead()
				return
			delNode = self.head
			currentPosition = 0
			while True:
				if currentPosition == position:
					previousNode.next = delNode.next
					delNode.next = None
					break
				previousNode = delNode
				delNode = delNode.next
				currentPosition += 1

	def isListEmpty(self):
		if self.head == None:
			return True
		else:
			return False

# Node => data, next
# firstNode.data => John , firstNode.next => None
linkedList = LinkedList()
linkedList.printList()
firstNode = Node("John")
linkedList.insertEnd(firstNode)
secondNode = Node("Ben")
linkedList.insertEnd(secondNode)
thirdNode = Node(10)
linkedList.insertAt(thirdNode, 10)
deleteNode = Node("Aish")
linkedList.insertEnd(deleteNode)
fourthNode = Node("Matthew")
linkedList.insertHead(fourthNode)
#linkedList.deleteEnd()
linkedList.deleteAt(3)
linkedList.printList()

