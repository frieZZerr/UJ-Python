# 'line' is defined as a string.
# 'result' should be the length of '_line'

line = 'one two 	three \n four'
_line = line.split()

result = sum( len(c) for c in _line )
print(result)