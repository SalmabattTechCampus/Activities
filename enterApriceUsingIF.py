price = int(input("enter price:"))

if price >100 :
    dis= price * (10/100)
    final_price = price - dis
    print (final_price)
else:
    dis= price * (5/100)
    final_price = price - dis
    print (final_price)
    
    