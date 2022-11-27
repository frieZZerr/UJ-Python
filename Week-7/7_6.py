import itertools
import random

bin_  = itertools.cycle( [0, 1] )
dir_  = iter( (lambda: random.choice( ("N", "E", "S", "W") ) ), 1 )
days_ = itertools.cycle( [x for x in range(7)] )

bin_arr  = []
dir_arr  = []
days_arr = []

for i in range(10):
	bin_arr.append ( next(bin_ ) )
	dir_arr.append ( next(dir_ ) )
	days_arr.append( next(days_) )

print( f"Binary: {bin_arr}" )
print( f"Directions: {dir_arr}" )
print( f"Days: {days_arr}" )