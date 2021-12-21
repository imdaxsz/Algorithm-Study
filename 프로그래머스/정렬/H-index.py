def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1, max(citations)+1):
        cnt = 0
        for k in citations[:i]:
            if i <= k:
                cnt+=1
        if cnt >= i and answer <= i:
                answer = i
    return answer
