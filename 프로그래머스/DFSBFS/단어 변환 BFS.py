def solution(begin, target, words):
    answer = 0
    queue = [begin]
    
    while True:
        word_list = []
        
        for word in queue:
            if word == target:
                return answer
            for i in range(len(words)-1, -1, -1):
                diff = sum([x!=y for x, y in zip(word, words[i])])
                if diff == 1:
                    word_list.append(words.pop(i))
                    
        if not word_list:
            return 0
        queue = word_list
        answer += 1
