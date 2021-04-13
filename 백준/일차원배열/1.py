A=[]
B=[]

n=int(input())
A = input().split(' ')

for i in range(n):
    B.append(int(A[i]))

print(min(B), max(B))
