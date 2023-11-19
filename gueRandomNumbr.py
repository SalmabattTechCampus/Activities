import  random
num = random.randint(1,10)
while(True):
    gus_number=int(input("enter a number:"))
    if (gus_number > num):
        print ("go down")
        continue
    elif (gus_number < num):
        print("go up")
        continue
    else:
        print(" correct number")
        break