import sys
input=sys.stdin.readline # 입출력 시간 줄일 수 있다. 

def compare(stack, com):
    size = len(stack)
    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'top':
        if size != 0:
            print(stack[size-1])
        else:
            print(-1)
    elif com[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'pop':
        if size != 0:
            print(stack[size-1])
            stack.pop()
        else:
            print(-1)
    elif com[0] == 'size':
        print(size)


stack = []

N = int(input())
for i in range(N):
    com = input().split()
    compare(stack, com)
    
