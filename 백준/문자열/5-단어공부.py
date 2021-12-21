n = list(input())
cnt = [0 for x in range(26)]

for k in n:
    a = ord(k)
    if a < 91:
        cnt[a-65] += 1
    else:
        cnt[a-97] += 1

ans = chr(cnt.index(max(cnt)) + 65)

cnt = sorted(cnt, reverse=True)
if cnt[0] == cnt[1]:
    print("?")
else:
    print(ans)
