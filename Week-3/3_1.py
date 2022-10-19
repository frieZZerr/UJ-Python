# Is the following code corrert?

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# You don't end line with a semicolon in Python

for i in "axby": if ord(i) < 100: print (i)
# Incorrect formatting

for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Incorrect formatting