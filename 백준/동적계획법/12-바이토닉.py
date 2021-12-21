n = int(input())
a = list(map(int, input().split()))
b = list(reversed(a))

inc = [1 for x in range(n)]
dec = [1 for x in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if b[i] > b[j]:
            dec[i] = max(dec[i], dec[j]+1)

dec.reverse()
result = [x+y-1 for x, y in zip(inc, dec)]
print(max(result))
