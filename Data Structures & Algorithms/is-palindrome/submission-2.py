class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""

        for i in range(len(s)):
            if s[i].isalnum():
                r += s[i].lower()

        return r[:] == r[::-1]
