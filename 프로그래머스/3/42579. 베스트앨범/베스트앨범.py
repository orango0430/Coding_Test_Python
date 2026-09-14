from collections import defaultdict
def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    songs = defaultdict(list)
    for i,g in enumerate(genres):
        total[g] += plays[i]
        songs[g].append((-plays[i],i))
    order = sorted((-v,k) for k,v in total.items())
    for v, genre in order:
        for play, i in sorted(songs[genre])[:2]:
            answer.append(i)
    return answer