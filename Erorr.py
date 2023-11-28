try:
    x=4/0
    print(x)
except ZeroDivisionError:
    print("can not divide by zero")
except:
    print("sth went wrong")