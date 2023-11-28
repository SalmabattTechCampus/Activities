file = open("test.txt.txt", "r")
print(file.readline())
  
  
  #-----------------------------------
file = open("txt.txt", "r")
lin = file.readline()
while (line !=""):
    line=file.readline()
    print(line)
    
#-----------------------------
    
file = open("numbers.txt", "r")
line = file.readline()
sum=0
count = 1
while (line !=""):
    line=file.readline()
    sum=float(line)
    sum+=float(line)
    count+=1
    print(sum/count)