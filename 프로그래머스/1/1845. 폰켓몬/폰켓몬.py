def solution(nums):
    answer = len(set(nums))
    choice = len(nums) // 2
    if choice < answer:
        return choice
    else:
        return answer