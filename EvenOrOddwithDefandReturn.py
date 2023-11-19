num = int(input("=>"))
def check_type(number):
    if (number%2 == 0):
        return "even"
    else:
      return "odd"
n = check_type(num)
print(n)