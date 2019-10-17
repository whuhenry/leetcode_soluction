class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        t = ''
        while l < r:
            t = s[l]
            s[l] = s[r]
            s[r] = t
            l += 1
            r -= 1
