#创建两个dict 然后遍历一个dict看是否在另外一个dict中，在的话append
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        result = []
        for i in nums1:
            if i not in dict1:
                dict1[i] = 0
            else:
                dict1[i] += 1
        for j in nums2:
            if j not in dict2:
                dict2[j] =0
            else:
                dict2[j] += 1
        
        for elements in dict1:
            if elements in dict2:
                result.append(elements)
        return result