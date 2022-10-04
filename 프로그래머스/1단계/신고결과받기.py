def solution(id_list, report, k):
    answer = [0 for x in range(len(id_list))]
    count = {x: 0 for x in id_list} #유저가 신고당한 횟수

    for r in list(set(report)):
        count[r.split()[1]] += 1
    
    for r in list(set(report)):
        if count[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer   
