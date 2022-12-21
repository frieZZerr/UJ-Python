class Item:

	def __init__( self, value, weight ):
		self.value  = value
		self.weight = weight
		self.proportion = value/weight

	def __lt__( self, other ):
		return self.proportion < other.proportion

	def __repr__(self):
		return "Item( %s, %s )" % ( self.value, self.weight )