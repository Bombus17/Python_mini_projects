# Authour: 	azmathias Stuperuser Ltd
# Purpose:	A program printing out every line to the song "99 bottles of beer on the wall"
# Notes:	Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics
#			Follow grammatic rules 


def sing(n):
	if (n == 1):
		objects = 'bottle'
		objectsMinusOne = 'bottles'
	elif (n == 2):
		objects = 'bottles'
		objectsMinusOne = 'bottle'
	else:
		objects = 'bottles'
		objectsMinusOne = 'bottles'


	if (n > 0):
		print(str(n) + " " + objects + " of beer on the wall, " + str(n) + " " + objects + " of beer.")
		print("Take one down and pass it around, " + str(n-1) + " " + objectsMinusOne + " of beer on the wall.")
		print(" ")
	elif (n == 0):
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall.")
	else:
		print("Error: Wheres the booze?")
bottles = 99

while bottles >= 0:
	sing(bottles)
	bottles -= 1
