def d(n):
    a = []    
    b = []

    for i in range(1, n+1):
        a.append(i)

    for j in range(1, n+1):
        sum = 0
        temp = list(str(j))
        for k in temp:
            sum += int(k)
        sum += j
        b.append(sum)

    c = [x for x in a if x not in b]

    for x in c:
        print(x)

d(10000)
