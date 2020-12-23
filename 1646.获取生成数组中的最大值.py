#
# @lc app=leetcode.cn id=1646 lang=python3
#
# [1646] 获取生成数组中的最大值
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        result = [0] * (n + 1)
        if n > 0:
            result[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                result[i] = result[i // 2]
            else:
                result[i] = result[i // 2] + result[i // 2 + 1]

        return result[n]
# @lc code=end

