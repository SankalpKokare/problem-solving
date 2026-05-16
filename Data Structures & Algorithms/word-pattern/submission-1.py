class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ctoWord = {}
        wtoChar = {}

        word = s.split(" ")

        if len(pattern) != len(word):
            return False

        for c, w in zip(pattern, word):
            if c in ctoWord and ctoWord[c] != w:
                return False
            if w in wtoChar and wtoChar[w] != c:
                return False
            ctoWord[c] = w
            wtoChar[w] = c

        return True
