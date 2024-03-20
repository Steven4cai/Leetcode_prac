#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, 
#then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

#二分搜索题目，首先二分法需要清楚我们的合法区间，以合法区间为左闭有闭为例子
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) //2
            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1
         
sol = Solution()
nums = [1,2,3,5,67,85,53,3]
result = sol.search(nums,6)
print(result)