N = int(input())
a = []

for i in range(1, N+1):
    temp = list(str(i))
    sum = 0
    for k in temp:
        sum += int(k)
    sum += i
    if sum == N:
      a.append(i)

if len(a) == 0:
    print(0)
else:
    print(min(a))
