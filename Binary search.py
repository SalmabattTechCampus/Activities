
def binary_search(key, lst):
    li, hi =0, len(lst) -1
    while(li<=hi):
        mid = int(hi+li)//2
        if(lst[mid] == key):
            return mid
        elif(lst[mid]<key):
            li = mid +1
        else:
            hi = mid - 1
            
    return -1
lst = [10,50,20,70,80,40,30]
lst.sort()
print(lst)
key = int(input("enter your targe: "))
result = print("your target is in index", binary_search(key, lst))
    