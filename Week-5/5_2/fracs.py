# calculate greatest common divsor
def gcd(a, b):
	if (a < b):
		return gcd(b, a)
	k = a
	while (k % b != 0):
		k += a
	return k

# frac1 + frac2
def add_frac(frac1, frac2):
	if frac1[1] == 0 or frac2[1] == 0:
		return

	_gcd = gcd( frac1[1], frac2[1] )
	mul1 = _gcd/frac1[1]
	mul2 = _gcd/frac2[1]

	frac1[0] = frac1[0]*mul1
	frac2[0] = frac2[0]*mul2

	return [ frac1[0]+frac2[0], _gcd]
	
# frac1 - frac2
def sub_frac(frac1, frac2):
	if frac1[1] == 0 or frac2[1] == 0:
		return

	_gcd = gcd( frac1[1], frac2[1] )
	mul1 = _gcd/frac1[1]
	mul2 = _gcd/frac2[1]

	frac1[0] = frac1[0]*mul1
	frac2[0] = frac2[0]*mul2

	return [ frac1[0]-frac2[0], _gcd]

# frac1 * frac2
def mul_frac(frac1, frac2):
	if frac1[1] == 0 or frac2[1] == 0:
		return

	return [ frac1[0]*frac2[0], frac1[1]*frac2[1] ]

# frac1 / frac2
def div_frac(frac1, frac2):
	if frac1[1] == 0 or frac2[1] == 0:
		return

	return [ frac1[0]*frac2[1], frac1[1]*frac2[0] ]

# bool, czy dodatni
def is_positive(frac):
	if frac[1] == 0:
		return

	if frac[0]*frac[1] > 0:
		return True
	return False

# bool, typu [0, x]
def is_zero(frac):
	if frac[1] == 0:
		return

	if frac[0] == 0:
		return True
	return False

# -1 | 0 | +1
def cmp_frac(frac1, frac2):
	if frac1[1] == 0 or frac2[1] == 0:
		return

	f1 = frac2float(frac1)
	f2 = frac2float(frac2)
	
	if f1 > f2:
		return -1
	elif f1 < f2:
		return 1
	else:
		return 0

# konwersja do float
def frac2float(frac):
	if frac[1] == 0:
		return

	return frac[0]/frac[1]