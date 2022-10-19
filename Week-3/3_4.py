# Check in a loop if the entered value by the user
#	if a float. Exit the program if input = stop

def IsFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

while(True):
	number = input("Enter a number: ")

	if IsFloat(number):
		print( "%s %s" % ( float(number), float(number) * float(number) ) )
	elif (number == "stop") :
		print("Exit")
		break
	else :
		print("It's not a number!")
		continue