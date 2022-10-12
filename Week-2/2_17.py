# 'line' is defined as a string.
# 'abc' should be 'line' sorted alphabetically
# '_len' should be 'line' sorted by words' length

line = "Guido van Rossum is a Dutch programmer"

abc  = sorted( line.split() )
_len = sorted( line.split(), key = len )

print(abc)
print(_len)