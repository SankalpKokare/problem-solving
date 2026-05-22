class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    
        res = -1
        first_ind = {}
        last_ind = {}

        for i, c in enumerate(s):
            if c not in first_ind:
                first_ind[c] = i
            else:
                last_ind[c] = i

        for c in last_ind:
            res = max(res, last_ind[c] - first_ind[c] - 1)

        return res