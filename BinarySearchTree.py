class Node:
	def __init__(self, value=None):
		self.value = value
		self.left_child = None
		self.right_child = None
class BST:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			self.insertNode(self.root, value)

	def insertNode(self, current_node, value):
		if value <= current_node.value:
			if current_node.left_child == None:
				current_node.left_child = Node(value)
			else:

				self.insertNode(current_node.left_child, value)

		elif value >= current_node.value:
                        if current_node.right_child == None:
                                current_node.right_child = Node(value)
                        else:

                                self.insertNode(current_node.right_child, value)
		else:
			print "Value already in tree!"

	def print_tree(self):
		if self.root != None:
			self.printTree(self.root)

	def printTree(self, current_node):
		if current_node != None:
			self.printTree(current_node.left_child)
			print str(current_node.value)
			self.printTree(current_node.right_child)

	def fill_tree(tree, number_elements=100, max_int=1000):
		from random import randint
		for _ in range(number_elements):
			current_element = randint(0, max_int)
			tree.insert(current_element)
		return tree


	def height(self):
		if self.root != None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self, current_node, current_height):
		if current_node == None: return current_height
		left_height = self._height(current_node.left_child, current_height+1)
		right_height = self._height(current_node.right_child, current_height+1)
		return max(left_height, right_height)

	def search(self, value):
		if self.root != None:
			return self._search(value,self.root)
		else:
			return False
		
	def _search(self, value, current_node):
		if value == current_node.value:
			return True
		elif value < current_node.value and current_node.left_child != None:
			self._search(value, current_node.left_child)
		elif value > current_node.value and current_node.right_child != None:
                        self._search(value, current_node.right_child)
		return False

tree = BST()
#tree = fill_tree(tree)

tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)

tree.print_tree()	
			
print "tree height: "+str(tree.height())	
		
