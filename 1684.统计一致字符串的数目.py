#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

from typing import List

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_set = set(allowed)
        result = 0
        for word in words:
            if set(word) <= allow_set:
                result += 1
        return result
# @lc code=end

s = Solution()
print(s.countConsistentStrings('ab', ["ad","bd","aaab","baa","badab"]))