# Authour:	azmathias Stuperuser Ltd
# Purpose:	Pythagorean Triples Checker
# 			Allows the user to input the sides of any triangle in any order.
# 			Return whether the triangle is a Pythagorean Triple or not.
# 			Loop the program so the user can use it more than once without having to restart the program.
# TODO:		Find a more elegant solution and optimise


import math

def pythag_triple(n0, n1, n2):
	triangle = []
	maxlen = 3
	while len(triangle) < maxlen:
		triangle.append(n0)
		triangle.append(n1)
		triangle.append(n2)
		triangle.sort()
	if triangle[2]  == math.sqrt(triangle[0] * triangle[0] + triangle[1] * triangle[1]):
		print("\nTriangle {0},{1},{2} IS a Pythagorean Triple".format(n0,n1,n2))
	else:
		print("\nTriangle {0},{1},{2} is NOT a Pythagorean Triple".format(n0,n1,n2))
	

def inputSides(message):
	while True:
		try:
			userinput = int(input(message))
		except ValueError:
			print("\nInput not recognised. Please input an integer:")
			continue
		else:
			return userinput
			break

def retestStatus():
	question =  "\nType q to quit, or hit <Enter> to test another triple."
	print(question)
	retestvalue = 0
	while not retestvalue:
		response = input('> ')
		if response == '':
			print()
		elif response == 'q':
			retestvalue = -1
		else:
			print("\nPlease try again.")
			print(testQ)
			continue
		return retestvalue
	

def main():
	welcome = """
				*************************************
					PYTHAGOREAN TRIPLES CHECKER
				*************************************
			"""
	print(welcome)
	retest = 0
	while retest != -1:	
		side1 = inputSides("Select a value  for side 1 of the triangle:")
		side2 = inputSides("Select a value for the second side:")
		side3 = inputSides("Select a value for the final side:")
		pythag_triple(side1, side2, side3)		
		retest = retestStatus()
	    

if __name__ == '__main__': main()

		
