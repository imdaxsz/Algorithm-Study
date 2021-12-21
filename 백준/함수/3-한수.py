N = int(input())

def h(n):
    ans = 0
    for i in range(1, N+1):
        temp = list(str(i))
        if i < 100:
            ans += 1
        else:
            if int(temp[1])-int(temp[0]) == int(temp[2])-int(temp[1]):
                ans += 1
    return ans

print(h(N))
