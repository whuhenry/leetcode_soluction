#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

from typing import List
# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
# @lc code=end

