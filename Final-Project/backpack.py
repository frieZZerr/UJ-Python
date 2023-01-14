from item import Item

class Backpack:

	def __init__(self):
		self.capacity = 0
		self.items = []
		self.value = 0

	#	Reading input
	def getData( self, file ):
		with open(file) as f:
			self.max_capacity = int( f.readline() )
			data = f.readlines()

		items_list = []
		#	Adding all of the items list
		for x in data:
			pair = x.split()
			item = Item( int(pair[0]), int(pair[1]) )
			items_list.append(item)

		items_list.sort()
		return items_list

	#	Finding most profitable items
	def findBestItems( self, items_list ):
		#	Iterating through all items
		while len(items_list) > 0:
			best_item = items_list.pop()
			
			#	Adding the item to the backpack
			if self.capacity+best_item.weight <= self.max_capacity:
				self.items.append(best_item)
				self.capacity += best_item.weight
				self.value += best_item.value

	#	Printing out items and their summed value
	def printItems(self):
		for item in self.items:
			print(item)
		print("Value=%s" % (self.value) )