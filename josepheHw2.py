

''' Assignment 2 - Conditionals
	Edward Joseph
	CSCD 110
	--No code pulled from outside sources--
'''
import datetime

now = datetime.datetime.now()

todayYear = now.year
todayMo = now.month
todayDay = now.day

#print (str(now))

print("Hello, welcome to Hopper's Computer Museum!")
print("To determine your entrance fee, please enter the ")
print("following: ")

dateValid = False

while (dateValid == False):

	userMo, userDay, userYear = input("Your Date of Birth (mm dd yyyy) --> ").split()

	 #Convert to int
	userMo = int(userMo)
	userDay = int(userDay)
	userYear = int(userYear)

	if userMo == '01' or userMo == '03' or userMo == '05' or userMo == '07' or userMo == '08' or userMo == '10' or userMo == '12':

		if 1 <= userDay <= 31:
			dateValid = True
		else:
			print ("Invalid date!")

	if userMo == '04' or userMo== '06' or userMo == '09' or userMo == '11':
		if 1 <= userDay <= 30:
			dateValid = True
		else:
			print("Invalid date!")

	else:
		if 1 <= userDay <= 28:
			dateValid = True
		else:
			print("Invalid date!")





coupon = input("Do you have a coupon? (y/n): ")

#Determine User Age
age =  todayYear - userYear

if userMo > todayMo:
	age = age - 1
elif userMo == todayMo and userDay > todayDay:
	age = age - 1


#Calc Price
if age <= 14:
	price = float(5.00)
elif age - userYear <= 64:
	price = float(9.00)
elif age - userYear >= 65:
	price = float(7.50)

#Discount with coupon
if coupon == "y" or coupon == "Y":
	price = price - 1

print("Your admission fee is $%d, enjoy your visit!" % price)
