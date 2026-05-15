class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        stoT = {}
        ttos = {}

        for i in range(len(s)):
            if s[i] in stoT and stoT[s[i]] != t[i]:
                return False

            if t[i] in ttos and ttos[t[i]] != s[i]:
                return False

            stoT[s[i]] = t[i]
            ttos[t[i]] = s[i]

        return True