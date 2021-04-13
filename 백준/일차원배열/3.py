A = []
B = []
C = []
cnt = 0

for i in range(42):
    C.append(0)

for i in range(10):
    x = int(input())
    B.append(x%42)
    A.append(x)

for j in range(10):
    C[B[j]] = C[B[j]]+1

for i in range(42):
    if C[i]>0:
        cnt = cnt+1

print(cnt)

    
