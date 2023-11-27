    
dic ={1:{'name':'jhon', 'age' :27,'sex':'male'},
      2:{'name':'Maria','age':22,'sex':'female'},
      3: {'name':'Sali','age':23,'sex':'female'}}


for key in dic:
        if (dic[key]['age'] > 22):
            print(dic[key]['name'], end=' ')