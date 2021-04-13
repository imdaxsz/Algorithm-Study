n = int(input())
A = []
B = []
sum = 0

A=input().split(' ')
for i in range(n):
    B.append(int(A[i]))
   

m = max(B)
for i in range(n):
    B[i] = B[i]/m*100
    sum += B[i]

print(B)
avg = sum/n
print(avg)


