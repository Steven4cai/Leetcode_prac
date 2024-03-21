#这道题难度并不大但是需要记得他每一次循环其实是按照规律从左到右，上到下，右到左，下到上
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0]* n for _ in range(n)]
        offset = 1
        count = 1
        loop = n//2
        sx, sy = 0,0
        mid = n//2
        for offset in range(1,loop + 1):
            for i in range(sy,n-offset):
                nums[sx][i] = count
                count += 1
            for j in range(sx,n-offset):
                nums[j][n-offset] = count
                count += 1
            for k in range(n-offset,sy,-1):
                nums[n-offset][k] = count
                count += 1
            for l in range(n-offset,sx,-1):
                nums[l][sy] = count
                count += 1
            sx += 1
            sy += 1
        if n%2 != 0:
            nums[mid][mid] = count
        return nums
        