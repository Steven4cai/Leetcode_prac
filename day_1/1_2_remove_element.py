
#这道题的思路是设置两个指针一个快指针一个慢指针，让快指针直接在for loop当中自己itera就行
#只有当与目标不符合，which is我们需要的元素，我们就需要将慢指针对应的下标的val替换成快指针对应的val并让慢指针++
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
    
             
sol = Solution()
nums = [1,2,3,5,67,67,53,4]
result = sol.removeElement(nums,67)
print(result)