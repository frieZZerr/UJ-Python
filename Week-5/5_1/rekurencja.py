
def fib(n):
	if n<2:
		return 1

	return fib(n-1)+fib(n-2)

def fac(n):
	if n == 1:
		return 1

	return n*fac(n-1)