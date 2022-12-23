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
def __init__( self, max_capacity ):
		self.max_capacity = max_capacity
		self.capacity = 0
		self.items = []
		self.value = 0
```

---

## `Algorithm`:

### 1. GetData()

First of all we're going to get the **data** from a given file:

```python
# Reading input
def getData(file):
	with open(file) as f:
		capacity = int( f.readline() )
		data = f.readlines()
```

Also initialize the ***backpack*** as well as add all of the items to the list:

```python
# Create backpack with given capacity
global backpack
backpack = Backpack(capacity)

# Initializing items list and adding them all to it
global items
items = []
for x in data:
  pair = x.split()
  item = Item( int(pair[0]), int(pair[1]) )
  items.append(item)
```

### 2. FindBestItems()

To find the _"best items"_ we iterate through the *items list*.

- `best_item` will be found by the *max()* function:

```python
def __lt__( self, other ):
  return self.proportion < other.proportion
```

<sup>*It's possible because `Item` class has overridden the `<` operator.</sup>

```python
# Iterating through all items
while len(items) > 0:
  best_item = max(items)

  # Adding the item to the backpack
  if backpack.capacity+best_item.weight <= backpack.max_capacity:
    backpack.items.append(best_item)
    backpack.capacity += best_item.weight
    backpack.value += best_item.value

  items.remove(best_item)
```

<sup>*After we found the _"best item"_, we check if there's space for it in the Knapsack and either we **add it** or **remove it** _(if there's not enough space for it)_.</sup>

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
