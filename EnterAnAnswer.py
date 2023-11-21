
answer = "abaacb"
user_answer = input("Enter your answer")
for i in range (len(answer)):
        if(user_answer[i] == answer[i]):
           mark+=1
print(mark,"out of", len(answer))