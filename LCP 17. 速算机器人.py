class Solution:
    def calculate(self, s: str) -> int:
        x = 1
        y = 0
        for ch in s:
            if ch == 'A':
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y