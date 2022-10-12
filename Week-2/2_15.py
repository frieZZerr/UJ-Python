# 'L' is a defined list.
# 'result' should be a string created from elements of 'L'

L = [ 5, 2, 9, 12, 4]

result = ''.join( str(i) for i in L )
print(result)