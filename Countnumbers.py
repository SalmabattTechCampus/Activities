Num= "123456789"
counter = 0
message = input("enter a numbr:")
for chr1 in message:
     if(chr1 in  Num):
        counter+=1
        print (counter)