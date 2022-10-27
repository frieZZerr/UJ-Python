
def make_ruler(_len):
    temp = ("|...")
    top = temp*_len + "|"
    bot = ""

    for i in range(0, _len+1):
        if i < 9:
            bot += str(i) + "   "
        else:
            bot += str(i) + "  "

    ruler = top + "\n" + bot
    return ruler

def make_grid(x, y):
    result = ""

    for i in range(0, y):
        result = result +  "+---" * x + "+\n"
        result = result + "|   " * x + "|\n"

    result = result + "+---" * x + "+\n"
    return result

if __name__ == "__main__":

    #RULER
    _len = int( input("Enter a length of the ruler: ") )
    print( make_ruler(_len) )

    #GRID
    x = int( input("Enter width: ")  )
    y = int( input("Enter height: ") )
    print( make_grid(x, y) )