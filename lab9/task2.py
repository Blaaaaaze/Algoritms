import random
A = [[random.randint(1, 100) for i in range(5)] for j in range(10)] #5 na 10
B = [[random.randint(1, 100) for i in range(100)] for j in range(10)]# 100 na 10
C = [[random.randint(1, 100) for i in range(5)] for j in range(100)]# 5 na 100
D = [[random.randint(1, 100) for i in range(5)] for j in range(2)]# 5 na 2
E = [[random.randint(1, 100) for i in range(4)] for j in range(5)]#4 na 5

matrix = []
matrix.append(A,B,C,D,E)
for i in range(len(matrix)):
    for i in range(len(matrix[i])):
        print(matrix[i][j])