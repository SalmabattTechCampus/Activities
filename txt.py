#file = open("salma.txt", "r")
#print(file.readline())



file2=open("text2.txt", "r")
for line in file2:
    line=line.split(" ")
    if(int(line[1]) > 70):
       print(line[0], "mark is", line[1])

  
  