## Edward Joseph
## Homework 4 - Conversion Calculator


def main():
    choice = displayMenu()
    while choice != '6':
        if choice == '1':            
            feetToMeters()
        elif choice == '2':
            metersToFeet()
        elif choice == '3':
            farToCel()
        elif choice == '4':
            celToFar()
        elif choice == '5':
            backwards()

        choice = displayMenu()
        
    print("\nThanks for playing!\n\n")
# ____________________________________________________________
# Menu function

def displayMenu():
    myChoice = '0'
    while myChoice != '1' and myChoice != '2' \
          and myChoice != '3' and myChoice != '4'\
              and myChoice != '5' and myChoice != '6':
        print("""\n\nPlease choose
                   1. Convert Feet to Meters
                   2. Convert Meters to Feet
                   3. Convert Farenheit to Celsius
                   4. Convert Celsius to Farenheit
                   5. Display a Phrase or Number Backwards
                   6. Quit
                   """)
        myChoice = input("Enter option--> ")
        
        if myChoice != '1' and myChoice != '2' and \
            myChoice != '3' and myChoice != '4'\
                and myChoice != '5' and myChoice != '6': 
            print("Invalid option.  Please select again.")

    return myChoice
# __________________________________________________________

#Where the magic happens

def feetToMeters():
    tempNum = float(input("Please enter feet: "))
    convNum = tempNum * 0.3048
    print ("Your number is %f meters" % convNum)
    input("\n\nPress Enter to continue")

def metersToFeet():
    tempNum = float(input("Please enter meters: "))
    convNum = tempNum * 3.28084
    print ("Your number is' %f 'feet" % convNum)
    input("\n\nPress Enter to continue")

def farToCel():
    tempNum = float(input("Please enter temperature in Farenheit: "))
    convNum = (tempNum - 32.0) / 1.8
    print ("Your temperature is %f degrees celsius" % convNum)
    input("\n\nPress Enter to continue")

def celToFar():
    tempNum = float(input("Please enter temperature in Celsius: "))
    convNum = tempNum * 1.8 + 32
    print ("Your temperature is %f degrees celsius" % convNum)
    input("\n\nPress Enter to continue")

def backwards():
    tempString = input ("Enter a text or a number to backwards-ify: ")
    print (tempString[::-1])
    input("\n\nPress Enter to continue")


main()
