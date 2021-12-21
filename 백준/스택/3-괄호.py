import sys
input=sys.stdin.readline


N = int(input())
ans = []

for i in range(N):    
    s = list(input().strip())
    ans.append("YES")
    stack = []
    
    for k in s:
        if k == '(':
            stack.append(k)
        if k == ')':
            if len(stack)<=0:
                ans[i] = "NO"
                break;
            else:
                stack.pop()
                
    if len(stack) != 0:
        ans[i]="NO"
        
for k in ans:
    print(k)

