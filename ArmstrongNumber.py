# Authour: 	azmathias Stuperuser Ltd
# Purpose:	Define a function that allows the user to check whether a given number is armstrong number or not.
#			Number x, no of digits = n, if the sum of each digit raised to the power of n is equal to x, the number is an armstrong number (also called narcisstic numbers)		
# Notes:	Examples of Armstrong Numbers are: 153, 407, 1634 

# get number to test
def inputNum(message):
	while True:
		try:
			userinput = int(input(message))
		except ValueError:
			print("\nPlease input a valid number:")
			continue
		else:
			return userinput
			break

# determine Armstrong number status			
def armstrongNumcheck(number):
	pownum = len(str(number))
	sum = 0
	resnum = number
	while resnum > 0:
		digit = resnum % 10
		sum += digit ** pownum
		resnum //= 10
	# return results
	if number == sum:
		print(number,"is an Armstrong number")
	else:
		print(number,"is not an Armstrong number")
		
# allow user to test again		
def testStatus():
	testQ = "\nType q to quit, or hit <Enter> to test another number."
	print(testQ)
	new_value = 0
	while not new_value:
		response = input('> ')
		if response == '':
			print()
		elif response == 'q':
			new_value = -1
		else:
			print("\nPlease try again.")
			print(testQ)
			continue
		return new_value

# program starts here
def main():
	print("Welcome to the Armstrong Number Checker \n")   
	value = 0
	while value != -1:
		num = inputNum("Please enter a number:")
		armstrongNumcheck(num)
		value = testStatus()
	print("\nThank you for playing!")
	

if __name__ == '__main__': main()
		


		

