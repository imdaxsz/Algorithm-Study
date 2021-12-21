N, M = input().split()
N = int(N)
M = int(M)

card = input().split()

max = 0

for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            sum = int(card[i]) + int(card[j]) + int(card[k])
            if sum > max and sum <= M:
                max = sum
print(max)



