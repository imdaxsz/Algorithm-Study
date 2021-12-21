import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville)>=2:
        m = heapq.heappop(scoville)

        if m >= K:
            break
        else:
            m2 = heapq.heappop(scoville)
            heapq.heappush(scoville, m+2*m2)
            answer += 1
        
    if scoville[0] <= K:
        answer = -1
        
    return answer
