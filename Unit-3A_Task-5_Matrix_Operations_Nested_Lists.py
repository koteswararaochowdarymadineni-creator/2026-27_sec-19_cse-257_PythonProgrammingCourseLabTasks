A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Addition:")
for i in range(2):
    for j in range(2):
        print(A[i][j] + B[i][j], end=" ")
    print()

print("Subtraction:")
for i in range(2):
    for j in range(2):
        print(A[i][j] - B[i][j], end=" ")
    print()

print("Multiplication:")
for i in range(2):
    for j in range(2):
        s = 0
        for k in range(2):
            s += A[i][k] * B[k][j]
        print(s, end=" ")
    print()