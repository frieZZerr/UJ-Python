from backpack import Backpack
from item import Item

#	Reading input
def getData(file):
	with open(file) as f:
		capacity = int( f.readline() )
		data = f.readlines()

	#	Create backpack with given capacity
	global backpack
	backpack = Backpack(capacity)

	#	Initializing items list and adding them all to it
	global items
	items = []
	for x in data:
		pair = x.split()
		item = Item( int(pair[0]), int(pair[1]) )
		items.append(item)

#	Finding most profitable items
def findBestItems():
	#	Iterating through all items
	while len(items) > 0:
		best_item = max(items)
		
		#	Adding the item to the backpack
		if backpack.capacity+best_item.weight <= backpack.max_capacity:
			backpack.items.append(best_item)
			backpack.capacity += best_item.weight
			backpack.value += best_item.value

		items.remove(best_item)

#	Printing out items and their summed value
def printItems():
	for item in backpack.items:
		print(item)
	print("Value=%s" % (backpack.value) )