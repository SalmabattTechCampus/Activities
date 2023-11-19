pin = "1234"
balane = 100
UserPin = (input("entr your pin:"))

if (pin == UserPin):

    choose=input("""choose :
                  1-check balance
                  2- withdraw
                  3- deposit
                  :""")
    if (choose ==1):
        print (balance)
    elif (choose==2):
        withdraw=int(input("enter the amount"))
        print ("your final balance is : "+str(balance-withdraw))
    else:
        deposit=int(input("enter how much deposit you want:"))
        print ("enter final balance: "+str(balance+deposit))
        
        
else:
        exit("wrong number")
            
    
       
    
 

