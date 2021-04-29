# 1차시도 100%
def solution(nums):
    return len(set(nums)) if len(set(nums)) <= len(nums) / 2 else len(nums) / 2