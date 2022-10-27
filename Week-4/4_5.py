
def it( L, left, right ):
	temp = 0
	while( right != left ):
		temp = L[left]
		L[left] = L[right]
		L[right] = temp
		right = right-1
		left = left+1
	return L

def rec( L, left , right ):
	temp = 0
	if left != right:
		temp = L[left]
		L[left] = L[right]
		L[right] = temp
		L = rec(L, left+1, right-1)
	return L

if __name__ == "__main__":
	list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print( "Before rotation: " )
	print( list )

	print( "=== Iteratively ===" )
	print( "After rotation: " )
	print( it(list, 0, 8) )

	print( "=== Recursively ===" )
	print( "After rotation: ")
	print( rec(list, 0, 8) )