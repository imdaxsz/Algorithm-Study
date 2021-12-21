import math
from itertools import permutations

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(perlist)):
            if check(int(j)):
                answer.append(int(j))
'''
    print(answer)
    print(set(answer))
'''
    answer = len(set(answer))

    return answer

num = "011"
print(solution(num))
