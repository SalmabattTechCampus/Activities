num = int(input("=>"))
def check_type(number):
    if (number%2 == 0):
        print("even")
    else:
        print("odd")
    check_type(num)
    