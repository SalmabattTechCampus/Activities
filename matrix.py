matrix = [[2,5,1],
         [4,9,0],
         [11,6,7]]
print(matrix[1][1])
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j]*2, end=" ")
        print()