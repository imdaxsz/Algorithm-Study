import sys
input=sys.stdin.readline

N = int(input())
n = 1

stack = []
ans = []

for i in range(N):
    num = int(input())
    if n > num and len(stack)==0:
        ans.append("NO")
        break;

    while(n <= num):
        stack.append(n)        
        ans.append("+")
        n+=1
            
    while(stack and stack[-1] >= num):
        ans.append("-")
        k = stack.pop()
        if k == num:
            break;

if ans[-1] == "NO":
    print("NO")
else:
    for a in ans:
        print(a)
