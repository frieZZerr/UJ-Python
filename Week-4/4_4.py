
def fibonacci(n):
    result = 0
    y = 1
    for i in range(0, n):
        last = result
        result = y
        y = last+y
    return result

if __name__ == "__main__":
    n = int( input("Enter number: ") )
    print( fibonacci(n) )