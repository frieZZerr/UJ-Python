# 'line' is defined as a string.
# 'first' should be a string created from first letter of each word in 'line'
# 'last' should be a string created from last letter of each word in 'line'

line = 'one two 	three \n four'
_line = line.split()

first = ""
last  = ""
for c in _line:
	first += c[0]
	last  += c[-1:]

print(first)
print(last)