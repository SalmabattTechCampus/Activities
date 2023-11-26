

# program enters a user number , the number goes to list called result,if the users enter Q it will print the result
result = []
while(true):
    n=input("enter a number:")
    if (n!= "Q"):
        result.append(int(n))
    else:
print (result)
            break