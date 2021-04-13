A = []

for i in range(9):
    x = int(input())
    A.append(x)

print(max(A))
print(A.index(max(A))+1)
