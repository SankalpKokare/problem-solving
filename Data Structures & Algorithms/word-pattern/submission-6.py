class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        pw = {}
        wp = {}

        for p, w in zip(pattern, words):
            if p in pw and pw[p] != w:
                return False
            if w in wp and wp[w] != p:
                return False

            pw[p] = w
            wp[w] = p

        return True
