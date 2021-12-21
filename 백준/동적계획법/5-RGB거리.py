import sys
input=sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        if j == 0:
            a[i][j] = a[i][j] + min(a[i-1][1], a[i-1][2])
        if j == 1:
            a[i][j] = a[i][j] + min(a[i-1][0], a[i-1][2])
        if j == 2:
            a[i][j] = a[i][j] + min(a[i-1][0], a[i-1][1])

print(min(a[n-1]))
