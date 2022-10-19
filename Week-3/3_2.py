# What's wrong with the following code?

L = [3, 5, 4] ; L = L.sort()
# List overwritten

x, y = 1, 2, 3
# Can't assign 3 values to 2 variables

X = 1, 2, 3 ; X[1] = 4
# Can't change elements in a tuple

X = [1, 2, 3] ; X[3] = 4
# Out of index bounds

X = "abc" ; X.append("d")
# Can't .append() on a string

L = list(map(pow, range(8)))
# Incorrect use of pow() function