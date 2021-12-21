def solution(progresses, speeds):
    a = []
    answer = []
        
    for i in range(len(speeds)):
        k = 100 - progresses[i]
        tmp = k // speeds[i]
        if k % speeds[i] > 0 :
            tmp += 1
        a.append(tmp)

    i = 0
    while(i<len(a)-1):
        b = 1
        j = i+1
        while(j < len(a) and a[i]>=a[j]):
            b += 1
            j += 1
        answer.append(b)
        i = j
        if j == len(a):
            break

    if sum(answer) < len(a):
        answer.append(1)
        
    return answer

'''
#TEST
p = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = solution(p, q)
print(ans)
'''
