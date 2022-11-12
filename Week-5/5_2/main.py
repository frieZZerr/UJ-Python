import fracs

if __name__ == '__main__':
	frac0 = [3, 5]
	frac1 = [1, 2]
	frac_neg = [1, -3]
	frac_zero = [0, 7]
	frac_null = [0, 0]

	print( "Add_Frac:" )
	print( f"{frac0} + {frac1} = { fracs.add_frac(frac0, frac1) }" )
	print( "Sub_Frac:" )
	print( f"{frac0} - {frac1} = { fracs.sub_frac(frac0, frac1) }" )
	print( "Mul_Frac:" )
	print( f"{frac0} * {frac1} = { fracs.mul_frac(frac0, frac1) }" )
	print( "Div_Frac:" )
	print( f"{frac0} / {frac1} = { fracs.div_frac(frac0, frac1) }" )
	print( "Is_Positive:" )
	print( f"{frac_neg} --> { fracs.is_positive(frac_neg) }" )
	print( "Is_Zero:" )
	print( f"{frac_zero} --> { fracs.is_zero(frac_zero) }" )
	print( "Frac2Float:" )
	print( f"{frac0} = { fracs.frac2float(frac0) }" )