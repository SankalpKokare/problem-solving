class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        r = len(s) - 1

        for i in range(len(s) // 2):
            s[i], s[r] = s[r], s[i]
            r -= 1
