
def binary_search(x):
    li, hi =1, x
    if (x==1 or x==0):
        return x
    while(li<=hi):
        mid = int(hi+li)//2
        if(mid * mid ==x):
            return mid
        elif(mid * mid < key):
            li = mid +1
        else:
            hi = mid - 1
            
    return -1

x= int(input("enter your targe: "))
result = print("your target is in index", binary_search(x))
    
