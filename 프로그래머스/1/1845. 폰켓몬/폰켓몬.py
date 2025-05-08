def solution(nums):
    temp = set(nums)
    
    if len(temp) >= len(nums) / 2:
        return len(nums) / 2
    
    return len(temp)