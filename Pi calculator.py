pi = 0
while 1:
    accuracy = input("How many repetitions would you like?")
    accuracy = int(accuracy)
    for i in range(0, accuracy):
        pi += ((4.0 * (-1)**i) / (2*i + 1))
        
    print("Pi is:", pi)
