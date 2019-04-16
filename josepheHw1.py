"""
Edward Joseph
This is 'Age at Graduation'
Assignment 1
100% original code
"""

#Introduction
print ("Welcome to the age calculator")

#Assign input variables
birthYear = int(input("Enter birth year: "))
birthMonth = int(input("Enter birth month: "))
birthDay = int(input("Enter birth day: "))
gradYear = int(input("Enter grad year: "))
gradMonth = int(input("Enter grad month: "))
gradDay = int(input("Enter grad day: "))

#run math on age change
gradAge =int(gradYear) - int(birthYear)

if birthMonth == gradMonth and birthDay < gradDay:
	gradAge = gradAge + 1 

#run math on months old using ageMonth variable
if birthMonth > gradMonth:
	ageMonth = int(birthMonth - gradMonth)
else:
	ageMonth = int(gradMonth - birthMonth)	

#print result
print ("You will be " + str(gradAge) + " years and " + str(ageMonth) + " months old when you graduate!")
