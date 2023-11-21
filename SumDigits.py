

def sum_digit(x):
     
     n= int(input("enter number :"))
     sum_=0
     while(n !=0):
         sum_+=n%10
         n=n//10
    
     return (sum_)
    result=sum_diit(234)
    print("sum of the numbr is :" +str(result))