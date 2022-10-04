def solution(dartResult):
    score = []
    mult = {'S':1,'D':2,'T':3}
    
    if '10' in dartResult:
        dartResult = dartResult.replace('10','t')
    result = [10 if i == 't' else i for i in dartResult]

    for i in range(1,len(result)):
        if result[i] in mult:
            score.append(int(result[i-1])**mult[result[i]])
        elif result[i] == '*':
            if i >= 4: score[-2] *= 2
            score[-1] *= 2
        elif result[i] == '#': score[-1] *= -1
    
    return sum(score)
