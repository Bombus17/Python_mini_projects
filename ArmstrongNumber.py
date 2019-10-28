# Authour: 	azmathias Stuperuser Ltd
# Purpose:	Define a function that allows the user to check whether a given number is armstrong number or not.
#			Number x, no of digits = n, if the sum of each digit raised to the power of n is equal to x, the number is an armstrong number (also called narcisstic numbers)		
# Notes:	All single digit numbers are armstrong numbers
# TODO:		Add more user input so users can check a number more than once, add error handling

print("Armstrong Number Checker \n")
num = int(input("Please enter a number"))

# calculate the length of the input number
pownum = len(str(num))

sum = 0

resnum = num
while resnum > 0:
	digit = resnum % 10
	sum += digit ** pownum
	resnum //= 10
	
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


