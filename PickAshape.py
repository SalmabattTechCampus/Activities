

def ShapeNum1 (x,a):
triangle=(b*h)/2
return triangle

def ShapeNum2(z,r):
squre=b*h
reurn squre
def ShapeNum3(y):
circle=(22/7*(n**2))
return circle

def ShapeNum4(w,s):
cylinder=(2*(22/7)*(n**2))+(2(22/7)*n*h)
return cylinder

pickaShape=0
while (pickaShape==pickaShape):
    if(pickaShape==1):
        h=int(input("enter the height:"))
        b=int(input("enter the base:"))
        result =ShapeNum1(b,h)
        print("the area of triangle"+str(result))
    elif (pickaShape==2):
        h=int(input("enter the length:"))
        b=int(input("enter the length:"))
        result =ShapeNum2 (b,h)
        print("the area of squre"+str(result))
    elif (pickaShape==3):
        n=int(input("enter the radius:"))
        result =ShapeNum3(n)
        print("the area of circle"+str(result))
    elif (pickaShape==4):
        n=int(input("enter the radius:"))
        h=int(input("enter the height:"))
        result =ShapeNum2 (n,h)
        print("the area of cylindar"+str(result))
    elif (pickaShape==5):
        print("exit")
        break