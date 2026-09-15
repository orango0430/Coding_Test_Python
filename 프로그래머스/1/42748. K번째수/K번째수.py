def solution(array, commands):
    answer = []
    result = []
    for i in commands:
        a = array[i[0]-1:i[1]]
        result.append(sorted(a))
    for k in range(0,len(result)):
        temp = commands[k][2] - 1
        answer.append(result[k][temp])
    return answer