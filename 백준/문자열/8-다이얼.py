t = list(input())
cnt = 0
a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for k in t:
    for i in range(len(a)):
        if k in str(a[i]):
            cnt += (i+3)
    
print(cnt)
