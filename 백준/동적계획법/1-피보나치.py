import sys
input=sys.stdin.readline

T = int(input())
ans = []

for i in range(T):
    N = int(input())
    if N == 0:
        ans.append([1, 0])
    else:
        cnt = [[0, 0] for x in range(N+1)]
        cnt[0] = [1, 0]
        cnt[1] = [0, 1]

        for i in range(2, N+1):
            cnt[i] = [x+y for x, y in zip(cnt[i-1], cnt[i-2])]

        ans.append([cnt[N][0], cnt[N][1]])

for i in range(T):
    print(ans[i][0], ans[i][1])
