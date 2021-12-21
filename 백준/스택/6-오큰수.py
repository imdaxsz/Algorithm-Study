import sys
input=sys.stdin.readline

N = int(input())
a = [int(x) for x in input().strip().split()]
nge = [-1 for _ in range(N)]
stack = []

stack.append(0)

for i in range(N):
    while stack and a[stack[-1]] < a[i]:
        nge[stack.pop()] = a[i]
    stack.append(i)

for k in nge:
    print(k, end=" ")
