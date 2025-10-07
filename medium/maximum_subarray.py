from typing import List

def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0];
    
    current_max = nums[0]
    res = nums[0]
    
    for i in range(1, len(nums)): #need to start from 1 since we already assigned nums[0]
        current_max = max(nums[i], current_max + nums[i])
        print(current_max)
        res = max(current_max, res)
        print(res)
   
    return res

nums = [5,4,-1,7,8]

maxSubArray(nums)