class Node(object):
	def __init__(self, val):
		self.val = val #is some value
		self.next = None #is an object

class SinglyLinkedList(object):
	def __init__(self):
		self.head = None #is first Node (object)
		self.tail = None #should always be none
	def PrintAllVals(self):
		runner = list.head
		while(runner.val):
			print runner.val
			if(runner.next):
				runner = runner.next
			else:
				break
	def AddBack(self, val):
		runner = list.head
		while(runner != None):
			if(runner.next == None):
				runner.next = Node(val)
				break
			runner = runner.next
	def AddFront(self, val):
		temp = list.head
		list.head = Node(val)
		list.head.next = temp
	def InsertBefore(self, nextVal, val):
		runner = list.head
		while(runner != None):
			# if next thing is the targeted value Node(nextVal)
			if(runner.next.val == nextVal):
				# runner.next should actually be Node(val)
				temp = Node(nextVal)
				runner.next = Node(val)
				runner.next.next = temp
				break
			runner = runner.next

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('PALL')
list.InsertBefore('Chad', 'Ben')
list.PrintAllVals()