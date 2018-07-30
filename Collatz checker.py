import time
import sys


def Collatz():
    global num
    global numcount
    numcount = 0
    
    print("This program was made from scratch without any help.")
    num = input("Which number would you like to test the Collatz Conjecture on?")
    num = str(num)
    if len(num) < 20:
        num = int(num)
        print(num)
        while num != 1:


            if num == 0:
                print("You can't enter zero.")
                break

                         
            elif num % 2 == 0:
                num /= 2
                numcount += 1
                num = int(num)
                print(num)

                
            elif num % 2 != 0:
                num *= 3
                num += 1
                numcount += 1
                num = int(num)
                print(num)

    
    elif len(num) > 20:
        print("Please note that this may take a long time to complete.")
        print("There is a big level of inacurracy because integers are only precise up to a certain amount of digits.")
        print("Ints can hold up to the number", sys.maxsize, "and are inaccurate for biger values.")
        time.sleep(10)
        num = int(num)
        print(num)
        while num != 1:


            if num == 0:
                print("You can't enter zero.")
                break

            
            elif num % 2 == 0:
                num /= 2
                numcount += 1
                num = int(num)
                print(num)

                
            elif num % 2 != 0:
                num *= 3
                num += 1
                numcount += 1
                num = int(num)
                print(num)

       
def main():
    Collatz()
    if num != 0:
        print("It took", numcount, "iterations to reach 1.")
    else:
        print("")

try:
    main()
except ValueError:
    print("Number either is not base 10 or is invalid.")
    

    
    
