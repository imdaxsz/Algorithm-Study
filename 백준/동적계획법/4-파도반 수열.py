import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    P = [1 for x in range(N)]
    for i in range(3, N):
        P[i] = P[i-3] + P[i-2]

    print(P[N-1])
