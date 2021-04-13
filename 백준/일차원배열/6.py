n = int(input())
ans = []

for i in range(n):
    A = list(input())
    score = 0
    total = 0
    if(A[0]=='O'):
        score = 1
        total = 1
    for k in range(len(A)):
       if k!=0:
           if A[k]=='X':
               score = 0
           if A[k]=='O':
               score += 1
               total += score
    ans.append(total)

for i in range(n):
    print(ans[i])
