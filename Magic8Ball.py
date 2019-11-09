# Authour: azmathias Stuperuser Ltd
# Purpose: Magic 8 Ball
#		Simulate a magic 8-ball.
#		Allow the user to enter their question.
#		Display an in progress message(i.e. "thinking").
#		Create 20 responses, and show a random response.
#		Allow the user to ask another question or quit.
# Bonus:
#	Add a gui.
#	It must have box for users to enter the question.
#	It must have at least 4 buttons:
#		ask
#		clear (the text box)
#		play again
#		quit (this must close the window)
# TODO: finish GUI


import random
import time


responses = ["Yes, most definitely!"
			, "The chances are high!"
			, "Not likely!"
			, "May the odds be in your favour."
			, "No chance kiddo!"
			, "99.9% success rate!"
			, "Congratulations, yes!"
			, "Ask again later!"
			, "Highly unlikely"
			, "Concentrate and ask again"
			]

def userquestion():
	question = input("\nYou may ask a question.\n")
	print("\nThinking...\n")
	time.sleep(random.randrange(0,4))
	print(random.choice(responses))

def main():
	print("Welcome to the Magic 8 Ball!")	
	while True:
		userquestion()
		repeat = input("Would you like to ask another question? (y/n)")
		if not (repeat == "y" or repeat == "Y"):
			print("\nThank you for playing!")
			break
		
if __name__ == '__main__': main()




		

	
	

