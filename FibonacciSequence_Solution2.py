#Author:	azmathias Stuperuser Ltd.
#Purpose:	Determine the nth number in the Fibonacci Sequence
#Notes:		Solution2: using recursion
#			[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
#ToDo: 		Combine solutions so user can choose which method to use in the same program
#			print sequence as well as nth term (for sequences < 10)
#

# get nth term to test
def inputterm(message):
	while True:
		try:
			userinput = int(input(message))
		except ValueError:
			print("\nPlease input a valid number:")
			continue
		else:
			return userinput
			break

def fibonacci2(n):
	if n < 0:
		print("Invalid input")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else: 
		return fibonacci2(n-1) + fibonacci2(n-2) 

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

def main():
	print("Fibonacci Sequence Term Finder (using recursion) \n")   
	value = 0
	while value != -1:
		num = inputterm("Please enter a number for the nth term:")
		ret_val = fibonacci2(num)
		print("\n{0} is the {1}th number in the Fibonacci Sequence".format(ret_val,num))
		value = testStatus()
	print("\nThank you for playing!")

if __name__ == '__main__': main()
