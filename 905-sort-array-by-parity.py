class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        even.extend(odd)
        return even