N, M = input().split()
N = int(N)
M = int(M)
chess = []

a = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
b = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']


for i in range(N):
    s = list(input())
    chess.append(s)

min = 2500

for i in range(N-7):
    for j in range(M-7):
        cnt = 0

        #비교 case1    
        for p in range(8):
            for q in range(8): 
                if p % 2 == 0:
                    if chess[i+p][j+q] != a[q]:
                        cnt += 1
                else:
                    if chess[i+p][j+q] != b[q]:
                        cnt += 1
        if min > cnt:
            min = cnt

        #비교 case2
        cnt = 0
        for p in range(8):
            for q in range(8):
                if p % 2 == 0:
                    if chess[i+p][j+q] != b[q]:
                        cnt += 1
                else:
                    if chess[i+p][j+q] != a[q]:
                        cnt += 1
        if min > cnt:
            min = cnt

print(min)


