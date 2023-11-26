dic = {1:"A", 2:"B"}
print(dic.get(2,"x"))
#----------------------------

dic = {1:"A", 2:"B"}
print(dic.pop(1))
print(dic)
#---------------------------

dic ={1:{"name":"ali", "age" :23},
      2:{"name":"muna","age":22}}

for key in dic:
    print(dic[key]["name"])
    
    
#---------------------------------dic ={1:{"name":"ali", "age" :23},
  
dic ={1:{"name":"ali", "age" :23},
      2:{"name":"muna","age":22}}

for key in dic:
    for key1 in dic[key]:
        print(dic[key][key1])