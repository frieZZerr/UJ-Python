from backpack import Backpack

data1 = 'data1.txt'
data2 = 'data2.txt'
data3 = 'data3.txt'

#	Initializing the backpack
b = Backpack()

#	Getting data
items_list = b.getData(data1)

#	Finding best items
b.findBestItems(items_list)

#	Printing items
b.printItems()