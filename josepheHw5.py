## Edward Joseph
## Hw5 - List Traversal
## Extra Credit attempted

#importing stat for easy and clean median code.
import statistics
myArray = []

def main():
    choice = displayMenu()
    while choice != '6':
        if choice == '1':            
            addNum()
        elif choice == '2':
            dispMean()
        elif choice == '3':
            dispMedian()
        elif choice == '4':
            showList()
        elif choice == '5':
            reverseList()
        choice = displayMenu()
        
    print("\nGoodbye!\n\n")
# ____________________________________________________________

# Just showing the menu here
def displayMenu():
    myChoice = '0'
    while myChoice != '1' and myChoice != '2' \
          and myChoice != '3' and myChoice != '4' \
          and myChoice != '5' and myChoice != '6':
        print("""\n\nPlease choose from the following:
                   1. Add a number to the list/array
                   2. Display the mean
                   3. Display the median
                   4. Print the list/array to the screen
                   5. Print the list/array in reverse order
                   6. Quit
                   """)
        myChoice = input("Enter option--> ")
        
        if myChoice != '1' and myChoice != '2' and \
            myChoice != '3' and myChoice != '4'\
            and myChoice != '5' and myChoice != '6': 
            print("Invalid option.  Please select again.")

    return myChoice
# __________________________________________________________


#Adding a number to the list
def addNum():
    theNum = -1
    while theNum < 0:
        try:
            theNum = int(input("Enter a number to add to the list: "))
            assert (theNum >= 0), "The number must be positive"   
            myArray.append(theNum)
        except ValueError:
            print("Please enter a positive INTEGER")
        except:
            print ("Number must be a positive integer")

    #pass

# calc the mean via python math
def dispMean():
    total = 0 
    for num in myArray:
       total += num
       mean = total / len(myArray)
    print (mean)

# initially had this as a mess of if statements, statistics.median() is much easier
# the assignment prompt didn't specify that we had to write it out, huehuehue
def dispMedian():
    # myArray = sorted(myArray)
    theMedian = statistics.median(myArray)
    print (theMedian)

# showing the myArray list, I felt it was weird not to sort it    
def showList():
    print (sorted(myArray))

#reversing the list, I like sorted's reverse = True more than [::-1]
def reverseList():
    print (sorted(myArray, reverse = True))
    



main()
