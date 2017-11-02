import os


"""
Pseudo code for the code:

1. Define a linked list class
2. Define a class to create the methods as defined in the questions.
	2.1. Store the head node in the class.
	2.2. Delete method:
		-> Check whether the head node value is equal to the given value.
			-> If its equal, then change the head node in the class to the next node in the linked list.
		-> If not:
			Don't change anything.
	2.3. Add method. 
		-> Check the position like where to add the node. 
		-> if the node has to be added in the front, 
			-> Create a new node with the given value.
			-> Link the head node to the present node
			-> change the head node to the present node in the class
		-> if the node has to be added in the end,
			-> Create a new node with the given value
			-> Use While loop to go to the last node
			-> Link the new node to the last node in the linked list.  
"""





class LinkedList(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class solutionClass(object):

	def __init__(self, listNode):
		self.head = listNode

	def delete(self, val):
		if (self.head.val==val):
			if(self.head.next!=None):
				self.head = self.head.next
			else:
				self.head = None
				print "As there is only one node in the linked list, it is deleted, as it is the first and the last element. "
		else:
			print "This Value cannot be deleted as it is not at the start of the linked list"

	def add(self,val,position):
		## Position: is an int argument given based on the position of the addition of the element. 
		if (position==0):
			newNode = LinkedList(val)
			newNode.next = self.head
			self.head = newNode
			print "New Value is added at the head of the linked list"
		elif(position ==1):
			newNode = LinkedList(val)
			node = self.node
			while(node.next != None):
				node = node.next
			node.next = newNode
			print "New value is added at the end of the linked list. "

def main():
	print "Hello World"
	node = LinkedList(1)
	node.next = LinkedList(2)
	node.next.next = LinkedList(3)
	node.next.next.next = LinkedList(4)
	node.next.next.next.next = LinkedList(5)

	x = solutionClass(node)
	x.delete(2)
	x.add(3,0)


if(__name__=='__main__'):
	main()