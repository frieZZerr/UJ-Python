# 'line' is defined as a string.
# 'result' should be the count of words in 'line'

line = 'one two 	three \n four'
result = line.split()
print( len(result) )