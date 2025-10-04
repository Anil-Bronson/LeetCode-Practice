from typing import List
# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.
def containsDuplicate(nums: List[int]) -> bool:
    found = set()

    for num in nums:
        if num in found:
            return True
        else:
            found.add(num)
    return False
            
nums = [1,2,3,1]
print(containsDuplicate(nums))


# shit code I wrote first:
    # found_map = {}

    # for num in nums:
    #     if num in found_map:
    #         if found_map[num] > 1:
    #             return True
    #         elif found_map[num] == 1:
    #                 return True
    #     else:
    #          found_map[num] = 1 #redundant
    
    # return False