def solution(n):
    prime = [0,0] + [1 for x in range(n-1)]
    for i in range(2, int(n**0.5)+1):
        if prime[i] != 0:
            for j in range(2*i, n+1, i):
                prime[j] = 0
    
    answer = len([x for x in prime if x == 1])
    return answer
