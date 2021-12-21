import heapq
def solution(operations):
    heap = []
    answer = []

    for operation in operations:
        op, num = operation.split(' ')
        if op == "I":
            heapq.heappush(heap, int(num))
        if op == "D":
            if num == '1' and heap:
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                #heap.pop(heap.index(max(heap)))
            if num == '-1' and heap:
                heapq.heappop(heap)

    if heap:
        answer = [heapq.nlargest(1,heap)[0], heap[0]]
    else:
        answer = [0, 0]
    return answer

print(solution(["I 7","I 7", "I 5","I -5","I -5", "D -1"]))
print(solution(["I 16","D 1"]))

# nlargest, nsmallest return list 
