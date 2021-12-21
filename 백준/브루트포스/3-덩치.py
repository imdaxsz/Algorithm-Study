N = int(input())
w = []
h = []
rank = []

for i in range(N):
    x, y = input().split()
    w.append(int(x))
    h.append(int(y))
    rank.append(1)

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if w[i] < w[j] and h[i] < h[j]:
            rank[i] += 1

for k in rank:
    print(k)
