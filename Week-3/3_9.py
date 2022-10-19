# Find a sum of elements in each element of a list

list1 = [ [], [4], (1,2), [3,4], (5,6,7) ]

result = list( map(sum , list1) )
print( result )