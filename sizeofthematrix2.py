#1 1 1 
#0 1 1
#0 0 1
            
size = int(input("enter the size"))
for i in range(size):
    for j in range(size):
        if (i<=j):
            print (1,end=" ")
        else:
            print(0, end=" ")
print()

          