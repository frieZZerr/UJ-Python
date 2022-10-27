
def sum_seq(sequence):
	if isinstance( sequence, (list, tuple) ):
		return sum( map( sum_seq, sequence ) )
	return sequence

if __name__ == "__main__":
    seq = [ 1, (2, 3), [], [4, (5, 6, 7)], 8, [9] ]
    print( "Sequence: " )
    print(seq)
    print( "Sum: " )
    print( str( sum_seq(seq) ) )