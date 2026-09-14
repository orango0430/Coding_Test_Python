from collections import Counter
def solution(participant, completion):
    answer = list((Counter(participant) - Counter(completion)))[0]
    return answer