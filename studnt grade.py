avg = 0
stu=int(input("number ofstudents"))
sum2 = 0
for i in range (1,stu+1):
    grade =float(input("enter a student grade:"))
    sum2 +=grade
    avg = sum2/4
    print (avg)