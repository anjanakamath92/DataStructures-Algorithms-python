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

# Node => data, next
# firstNode.data => John , firstNode.next => None
linkedList = LinkedList()
linkedList.printList()
firstNode = Node("John")
linkedList.insertEnd(firstNode)
secondNode = Node("Ben")
linkedList.insertEnd(secondNode)
thirdNode = Node("Matthew")
linkedList.insertHead(thirdNode)
linkedList.printList()

