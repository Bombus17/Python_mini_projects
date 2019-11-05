# Authour: 	azmathias Stuperuser Ltd
# Purpose:	A program that prints out a multiplication table up to and including a given number.
# TODO:		Error handling					
#  


def main():
	print("Multiplication Table Generator \n")
	rows = int(input("What is the upper bound of multiplication table? "))
	print("\nThe multiplication table for 2 to", rows)
	print()
	counter = 0
	multiplicationTable(rows,counter)
 
def multiplicationTable(rows,counter):
    size = rows + 1
    for i in range(1,size):
        for nums in range (1,size):
            value = i*nums
            print(value,sep=' ',end="\t")
            counter += 1
            if counter%rows == 0:
                print()
            else:
                counter
                
          
if __name__ == '__main__': main()
