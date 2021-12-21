def solution(n, computers):
    answer = 0
    visited=[False for i in range(n)]
    for i in range(n):
        if visited[i]==False:
            dfs(computers, i, visited)
            answer += 1
    return answer

def dfs(computers, com, visited):
    visited[com] = True
    for i in range(len(visited)):
        if com != i and computers[com][i]==1:
            if visited[i]==False:
                dfs(computers, i, visited)
                
