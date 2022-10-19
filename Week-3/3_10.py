# Create a dictionary for translating romaniam numbers

x = input( "Enter a Roman numeral: " )
values = { 'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
result = 0
for i in range( len(x) ):
    if i+1 < len(x) and values[ x[i] ] < values[ x[i + 1] ] :
        result = result - values[ x[i] ]
    else:
        result = result + values[ x[i] ]
print( result )