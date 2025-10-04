from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Given two integer arrays nums1 and nums2, 
    return an array of their intersection. 
    Each element in the result must be unique 
    and you may return the result in any order.
    """
    intersec = []
    for n1 in set(nums1):
        for n2 in set(nums2):   #O(n^2) worst case
            if n1 == n2:
                intersec.append(n1)
    
    return intersec

# optimal solution:
# return list(set(nums1) & set(nums2)) O(n + m) Intersecting them is O(min(n, m))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums3 = [1,2,2,1]
nums4 = [2,2]
print(intersection(nums3,nums4))