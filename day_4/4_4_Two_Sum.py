#最基本的hashing题型，我们我们只需要找target-element是否在之前出现过即可
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp not in result:
                result[nums[i]] = i
            else:
                return [result[temp],i]

        