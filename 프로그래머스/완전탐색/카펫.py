import math

def solution(brown, yellow):
    answer = []
    k = int(math.sqrt(yellow))
    for i in range(1, k+1):
        if yellow % i == 0:
            w = int(yellow / i)
            if (2*i + 2*w + 4) == brown:
                answer.append(w+2)
                answer.append(i+2)

    return answer


print(solution(10,2))
print(solution(8,1))
print(solution(18,6))
