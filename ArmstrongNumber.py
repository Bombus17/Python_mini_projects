# Authour: 	azmathias Stuperuser Ltd
# Purpose:	Define a function that allows the user to check whether a given number is armstrong number or not.
#			Number x, no of digits = n, if the sum of each digit raised to the power of n is equal to x, the number is an armstrong number (also called narcisstic numbers)		
# Notes:	All single digit numbers are armstrong numbers
# TODO:		Add error handling

testing_active = True

print("Armstrong Number Checker \n")

while testing_active:

		num = int(input("Please enter a number:"))
		
		# calculate the length of the input number
		pownum = len(str(num))
		
		sum = 0
		
		# determine Armstrong number status
		resnum = num
		while resnum > 0:
			digit = resnum % 10
			sum += digit ** pownum
			resnum //= 10
		
		# return results
		if num == sum:
			print(num,"is an Armstrong number")
		else:
			print(num,"is not an Armstrong number")
		
		# test again? 
		repeat = input("\nWould you like to test another number? (y/n) ")
		if repeat == 'n':
			testing_active = False

		

