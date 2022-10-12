# 'line' is defined as a string.
# 'word' should be the longest word in '_line'
# '_max' should be the length of 'word'

line = 'one two 	three \n four'
_line = line.split()

word = ""
_max = 0
for c in _line:
	if _max <= len(c):
		_max = len(c)
		word = c

print(word)
print(_max)