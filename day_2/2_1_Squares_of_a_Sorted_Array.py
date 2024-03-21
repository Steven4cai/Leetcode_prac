#这道题的思路是使用双指针的思路，因为对于一个sorted array，他的每个element的平方的最大值一定会出现在两端，我们只需要重新创建一个
#result array然后创建两个指针分别指向开头和结尾然后比较平方的大小
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        itera = len(nums) - 1
        while i <= j:
            if nums[i] * nums[i] < nums[j] * nums[j]:
                result[itera] = nums[j] * nums[j]
                itera -= 1
                j -= 1
            else:
                result[itera] = nums[i] * nums[i]
                itera -= 1
                i += 1
        return result

sol = Solution()
nums = [-4,-1,0,3,10]
print(sol.sortedSquares(nums))