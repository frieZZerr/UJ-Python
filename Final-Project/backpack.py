class Backpack:

	def __init__( self, max_capacity ):
		self.max_capacity = max_capacity
		self.capacity = 0
		self.items = []
		self.value = 0