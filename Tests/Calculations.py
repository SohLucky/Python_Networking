# Calculations

def menu():
    print('''=====================
	     (1) - Addition\n
	     (2) - Subtraction\n
	     (3) - Division\n
	     (4) - Mutiplication\n
	     (5) - Done\n
	     =====================
	  ''')
def ask_num():
    num = int(input("What number do you want to input: "))
    return num


option = 0
final = 0
num = 0
#Input a number in the event the user wants to do division or mutiplication
final = int(input("Number to start with: "))

while True:
    #Prints the Menu
    menu()

    #Takes User Input on which option to run
    option = int(input("Which option do you want to run?: "))
    
    
    #Addition
    if option == 1:
	final += ask_num()
	print "Current Sum: %d" % final
    
    #Subtraction
    elif option == 2:
	final -= ask_num()
	print "Current Sum: %d" % final

    #Division
    elif option == 3:
	number = ask_num()
	remainder = final % number
	final = final / number
	print "Current Sum: %d \nRemainder: %d" % (final, remainder)

    #Mutiplication
    elif option == 4:
	final = final * ask_num()
	print "Current Sum: %d" % final

    #End of Equation
    elif option == 5:
	print("Thank you for using this application\nFinal Sum: %d" % final)
	break
    else:
	print("Error")
	break


