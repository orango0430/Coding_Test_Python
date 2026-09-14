def solution(clothes):
    answer = 1
    d = {}
    for name,kind in clothes:
        d[kind] = d.get(kind,0) + 1
    for i in d.values():
        answer *= (i + 1)
    return answer - 1