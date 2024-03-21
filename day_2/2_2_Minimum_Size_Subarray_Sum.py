#这道题的解题思路是使用滑动窗口的思路，这道题目的意思是在整个array当中寻找最小的连续的整数数量使他们的sum 大于等于target
#滑动窗口的关键就在于首先第一点我们要iterate的是起始位置还是结束位置，我们在这道题当中应该使用结束位置因为如果iterate
#起始位置那么他其实就相当于是使用两个for loop，这道题当中我们iterate结束位置，关键在于我们如何更新初始位置
#在这里会使用while来持续更新起始位置直到小于target

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        i = 0
        result = len(nums) + 2
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                subL = j - i + 1
                result = min(result,subL)
                sum -= nums[i]
                i += 1
        
        if result == len(nums) + 2:
            return 0
        else:
            return result
        
sol = Solution()
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(7,nums))
