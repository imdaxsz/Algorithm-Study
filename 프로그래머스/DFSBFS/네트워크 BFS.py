def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i]==False:
            bfs(i, visited, computers)
            answer += 1
    return answer

def bfs(com, visited, computers):
    visited[com]=True
    queue = []
    queue.append(com)
    while(queue):
        u = queue.pop(0)
        for i in range(len(visited)):
            if i!=u and computers[u][i]==1:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]=True
        
