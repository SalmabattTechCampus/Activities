A=int(input("enter number 1:"))
B=int(input("enter number 2:"))
C=int(input("enter number 3:"))

if(A>=B and A>=C):
    print(str(A)+"is the largest")
elif(B>=A and B>=C):
    print(str(B)+"is the largest")
elif(C>=A and C>=B):
    print(str(C)+"is the largest")
else:
    print("")
       