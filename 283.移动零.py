#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

from typing import List

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[head] = nums[i]
                head += 1
        for i in range(head, len(nums)):
            nums[i] = 0
# @lc code=end

