# The Knapsack Problem

### What's the problem?
> "The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include
> in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible."

<sup>Source: ***wikipedia.org***</sup>

### How does it work?
We simply pick the *items* that have the **best proportions**, that is `item.value/item.weight`.

<sup>*The higher the proportion's value, the more valuable the item is ***(at the moment!)***.</sup>

### `Item Class`:

`Item` has *3 variables*:

```python
def __init__( self, value, weight ):
    self.value  = value
    self.weight = weight
    self.proportion = value/weight
```

As well as overridden `<` operator and `__repr__` method:

```python
def __lt__( self, other ):
		return self.proportion < other.proportion

	def __repr__(self):
		return "Item( %s, %s )" % ( self.value, self.weight )
```

### `Backpack Class`:

`Backpack` has *4 variables*:

```python
def __init__( self ):
		self.capacity = 0
		self.items = []
		self.value = 0
```

<sup>*One variable - `max_capacity`, is set in `getData()` function.</sup>

### 1. GetData()

First of all we're going to get the **data** from a given file:

```python
# Reading input
def getData( file, self ):
	with open(file) as f:
		self.max_capacity = int( f.readline() )
		data = f.readlines()

```

Also initialize the ***backpack*** as well as add all of the items to the list:

```python
#	Adding all the items to the list
items_list = []
for x in data:
	pair = x.split()
	item = Item( int(pair[0]), int(pair[1]) )
	items_list.append(item)

#	Sorting items list
items_list.sort()
return items_list
```

### 2. FindBestItems()

To find the _"best items"_ we iterate through the *items_list*.

- current `best_item` is the last item in sorted `items_list`:

```python
#	Iterating through all items
while len(items_list) > 0:
	best_item = items_list.pop()

	#	Adding the item to the backpack
	if self.capacity+best_item.weight <= self.max_capacity:
		self.items.append(best_item)
		self.capacity += best_item.weight
		self.value += best_item.value
```

<sup>*After we found the _"best item"_, we check if there's space for it in the Knapsack and either we **add it** or **remove it** _(if there's not enough space for it)_.</sup>

---

### 3. PrintItems()
                                                                
This method prints all items that are in the backpack sorted descending by `proportion`'s value and their summed `value`:
    
```python
# Printing out items and their summed value
def printItems():
	for item in backpack.items:
		print(item)
	print("Value=%s" % (backpack.value) )
```
                                                                
### Data input:
Data format is simple:
- first line is the `capacity` of the *backpack*,
- `item_value [tab] item_weight`, e.g.:

```
120 5
```
                                                                
---

### Example outputs for given datas:

- ***data1.txt***:
```
Item( 185, 3 )
Item( 60, 1 )
Item( 50, 2 )
Item( 120, 5 )
Item( 45, 2 )
Item( 200, 10 )
Item( 20, 1 )
Value=680
```

- ***data2.txt***:
```
Item( 160, 1 )
Item( 70, 1 )
Item( 70, 3 )
Item( 130, 6 )
Item( 40, 2 )
Item( 120, 7 )
Item( 35, 5 )
Item( 25, 4 )
Value=650
```
                                                                
- ***data3.txt***:
```
Item( 160, 1 )
Item( 60, 1 )
Item( 70, 3 )
Item( 75, 4 )
Item( 120, 7 )
Value=485
```
