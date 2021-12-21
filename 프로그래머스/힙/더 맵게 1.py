import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        m = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m+2*m2)
        answer += 1
        
        if len(scoville)==1 and scoville[0] <= K:
            return -1
        
    return answer


print(solution([3,10], 5))
