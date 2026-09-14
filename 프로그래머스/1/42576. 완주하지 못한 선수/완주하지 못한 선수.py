def solution(participant, completion):
    answer = ''
    temp = 0
    d = {}
    for part in participant:
        d[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= int(hash(com))
    answer = d[temp]
    return answer