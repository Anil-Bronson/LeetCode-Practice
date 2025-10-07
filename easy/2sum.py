from typing import List

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# O(n^2) solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for n in range(len(nums)):
        for i in range(n + 1, len(nums)):
            if nums[n] + nums[i] == target:
                return [n, i]
    return []

def twoSum2(self, nums: List[int], target: int) -> List[int]:
    map = {}

    for i,n in enumerate(nums):
        compliment = target - n
        if compliment in map:
            return [map[compliment], i]
        map[n] = i
    
    return []


