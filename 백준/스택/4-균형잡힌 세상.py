import sys
input=sys.stdin.readline

ans = []
idx = -1

while(True):
    str = input().rstrip()
    if str == '.':
        break;
    s = list(str)
    
    ans.append("yes")
    idx += 1
    stack = []

    for k in s:
        if k=='[' or k=='(':
            stack.append(k)
        if k==')':
            if len(stack)<=0:
                ans[idx]="no"
                break;
            if stack[len(stack)-1]=='[':
                ans[idx]="no"
                break;
            if stack[len(stack)-1]=='(':
                stack.pop()
        if k==']':
            if len(stack)<=0:
                ans[idx]="no"
                break;
            if stack[len(stack)-1]=='(':
                ans[idx]="no"
                break;
            if stack[len(stack)-1]=='[':
                stack.pop()

    if len(stack) != 0:
        ans[idx]="no"


for k in ans:
    print(k)
