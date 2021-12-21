import heapq
def solution(jobs):
    answer, start, now, complete = 0, -1, 0, 0
    jobs_heap = []

    while complete < len(jobs):
        for job in jobs:
            # 작업을 입력받은 시점이 시작 시간과 현재 시간의 사이인 경우
            if start < job[0] <= now:
                heapq.heappush(jobs_heap, [job[1], job[0]])
        if jobs_heap:
            min_job = heapq.heappop(jobs_heap)
            # 시작 시간에 현재 시간 입력
            start = now
            # 현재 시간에 최소 시간 작업을 처리한 시간 입력
            now += min_job[0]
            # answer에 현재 시간 - 최소 시간 작업을 입력받은 시점 입력
            answer += now - min_job[1]
            complete += 1
        else:
            now += 1

    return answer//len(jobs)
