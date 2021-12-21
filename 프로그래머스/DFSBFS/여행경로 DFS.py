from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)
    print(routes)

    stack = ['ICN']
    while stack:
        print("s:", stack)
        print("a:", answer)
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer

c = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"],
     ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"],
     ["COO", "BOO"], ["BOO", "AOO"]]
print(solution(c))
