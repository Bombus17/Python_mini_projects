# Authour: 	azmathias Stuperuser Ltd
# Purpose:	This program uses a function that allows the user to find the value of the nth term in the sequence by inputting the desired term. 
# Notes:	This solution uses a loop (less performant at as n increases). 
# 			[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181....]
# ToDo: 	More testing 

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

# return Fibonacci sequence to nth term
def fibonacci(nth):
	n1,n2 = 0,1
	for i in range(0,nth-1):
		n1,n2 = n2, n1+n2
	return(n1)

				
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
	print("Fibonacci Sequence Term Finder \n")   
	value = 0
	while value != -1:
		num = inputterm("Please enter a number for the nth term:")
		print(fibonacci(num))
		value = testStatus()
	print("\nThank you for playing!")
	
    

if __name__ == '__main__': main()

