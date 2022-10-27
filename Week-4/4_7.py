
def flatten( sequence ):
    if isinstance( sequence, (list, tuple) ):
        result = []
        if sequence:
            result += flatten( sequence[0 ] )
            result += flatten( sequence[1:] )
        return result
    else:
        return [sequence]

if __name__ == "__main__":
    seq = [ 1, (2, 3), [], [4, (5, 6, 7)], 8, [9] ]
    print( "Sequence: " )
    print( seq )
    print( "Flattened: " )
    print( flatten(seq) )