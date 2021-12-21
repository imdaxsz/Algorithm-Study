n, c = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for x in range(c+1)] for i in range(n+1)]

for i in range(1, n+1):
    for w in range(1, c+1):
        if a[i-1][0] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-a[i-1][0]]+a[i-1][1])

print(dp[n][w])
