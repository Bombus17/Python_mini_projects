# Authour: 	azmathias Stuperuser Ltd
# Purpose: Pythagorean Triples Checker
# 		Allows the user to input the sides of any triangle in any order.
# 		Return whether the triangle is a Pythagorean Triple or not.
# 		Loop the program so the user can use it more than once without having to restart the program.

import math

def pythagorean_triplet(a, b, c):
	for b in range(n):
		for a in range(1, b):
			c = math.sqrt(a * a + b * b)
			if c % 1 == 0:
				print(a, b, int(c))
				
pythagorean_triplet(1,2,3)			
