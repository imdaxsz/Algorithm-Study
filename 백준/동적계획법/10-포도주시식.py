n = int(input())
a = []
d = [0 for x in range(n)]

for i in range(n):
    a.append(int(input()))

d[0] = a[0]

if n >= 2:
    d[1] = a[0] + a[1]
if n >= 3:
    d[2] = max(d[1], a[0]+a[2], a[1]+a[2])

if n >= 4:
    for i in range(3, n):
        d[i] = max(d[i-3]+a[i-1]+a[i], d[i-2]+a[i])
        d[i] = max(d[i-1], d[i])

print(max(d))
