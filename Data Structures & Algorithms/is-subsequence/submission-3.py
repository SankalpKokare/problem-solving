class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = r = 0

        while len(s) > l and len(t) > r:
            if s[l] == t[r]:
                l += 1

            r += 1

        return len(s) == l
