n = int(input())
d = [0 for x in range(n)]
a = list(map(int, input().split()))

d[0] = a[0]
    
for i in range(1, n):
    d[i] = max(a[i], d[i-1]+a[i])

print(max(d))
