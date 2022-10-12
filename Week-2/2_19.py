# 'L' is a defined list.
# 'result' should be 'L' with '0' in front of numbers < 100

L = [ 4, 2, 1, 42, 24, 11, 420, 240, 111 ]

result = ' '.join( str(i).zfill(3) for i in L )
print(result)