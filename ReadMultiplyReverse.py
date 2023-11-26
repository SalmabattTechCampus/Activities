def read_float(n):
    result = []
    for i in range(n):
        num = float(input("entr a number"))
        result.append(num)
        return result
def multiply(ls,factor):
     for i in range(len(ls)):
     ls[i]= ls[i]*factor
     return ls
    
def print_reverse(ls):
     ls.reverse()
     return ls

def main():
    my_list = read_float(4)
    number = int(input("enter the factor"))
    my_list= multiply(my_list, number)
    print(new_list)
    print(my_list)
    final_list= print_reverse(new_list)
    print(final_lis)
    main()
