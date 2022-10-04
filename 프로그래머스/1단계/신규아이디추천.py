def solution(new_id):
    answer = ''

    # step 1
    answer = new_id.lower()
    
    # step 2
    delete = '~!@#$%^&*()=+[{]}:?,<>/'
    for d in delete:
        answer = answer.replace(d, '')

    # step 3
    while ('..' in answer):
        answer = answer.replace('..', '.')

    # step 4
    if answer[0] == '.':
        answer = answer[1:]  if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # step 5
    if answer == '':
        answer = 'a'
        
    # step 6
    if len(answer)>15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    # step 7
    while len(answer)<3:
        answer += answer[-1]
    
    return answer
