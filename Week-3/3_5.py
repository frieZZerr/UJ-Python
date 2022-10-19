# Print on screen a ruller

chunk = ( "|..." )
length = int( input("Enter a length of the ruler: ") )
print( chunk*length + "|" )

for i in range( length+1 ):
    if i < 9:
        print( i, end = '' )
        print( "   ", end = '' )
    else:
        print( i, end = '' )
        print( "  ", end = '' )